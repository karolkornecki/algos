import edu.princeton.cs.algs4.FlowEdge;
import edu.princeton.cs.algs4.FlowNetwork;
import edu.princeton.cs.algs4.FordFulkerson;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
// score 100/100
public class BaseballElimination {
    // create a baseball division from given filename in format specified below
    private final int numberOfTeams;
    private final String[] teams;

    private final int[] wins;
    private final int[] losses;
    private final int[] remaining;

    private final int[][] against;

    public BaseballElimination(String filename) {
        In in = new In(filename);
        String[] lines = in.readAllLines();
        numberOfTeams = Integer.parseInt(lines[0]);
        teams = new String[numberOfTeams];
        wins = new int[numberOfTeams];
        losses = new int[numberOfTeams];
        remaining = new int[numberOfTeams];
        against = new int[numberOfTeams][numberOfTeams];
        int offset = 4;
        for (int i = 1; i < lines.length; i++) {
            String[] t = lines[i].trim().split("\\s+");
            teams[i - 1] = t[0];
            wins[i - 1] = Integer.parseInt(t[1]);
            losses[i - 1] = Integer.parseInt(t[2]);
            remaining[i - 1] = Integer.parseInt(t[3]);
            for (int j = offset; j < offset + numberOfTeams; j++) {
                against[i - 1][j - offset] = Integer.parseInt(t[j]);
            }
        }
    }

    // number of teams
    public int numberOfTeams() {
        return numberOfTeams;
    }

    // all teams
    public Iterable<String> teams() {
        return Arrays.asList(teams);
    }

    // number of wins for given team
    public int wins(String team) {
        validate(team);
        return wins[id(team)];
    }

    // number of losses for given team
    public int losses(String team) {
        validate(team);
        return losses[id(team)];
    }

    // number of remaining games for given team
    public int remaining(String team) {
        validate(team);
        return remaining[id(team)];
    }

    // number of remaining games between team1 and team2
    public int against(String team1, String team2) {
        validate(team1);
        validate(team2);
        return against[id(team1)][id(team2)];
    }

    // is given team eliminated?
    public boolean isEliminated(String team) {
        validate(team);
        return elimination(team).eliminated;
    }


    // subset R of teams that eliminates given team; null if not eliminated
    public Iterable<String> certificateOfElimination(String team) {
        validate(team);
        Elimination elimination = elimination(team);
        if (!elimination.eliminated) {
            return null;
        }
        List<String> eliminatedBy = new ArrayList<>();
        if (elimination.isTrivialCase) {
            for (int i = 0; i < teams.length; i++) {
                if (wins[id(team)] + remaining[id(team)] < wins[i]) {
                    eliminatedBy.add(teams[i]);
                }
            }
        } else {
            for (int i = 0; i < teams.length; i++) {
                if (i != id(team)) {
                    if (elimination.maxFlow.inCut(i)) {
                        eliminatedBy.add(teams[i]);
                    }
                }
            }
        }
        return eliminatedBy;
    }

    private Elimination elimination(String team) {
        // Trivial elimination
        if (isTrivialElimination(team)) {
            return new Elimination(true);
        }

        int numberOfMatches = numberOfMatches(team);
        int totalNumberOfGamesBetweenTeams = 0;
        FlowNetwork network = new FlowNetwork(numberOfMatches + numberOfTeams + 2); // +2 means S and T artificial nodes
        int game = numberOfTeams;
        int S = network.V() - 1;
        int T = network.V() - 2;
        for (int i = 0; i < against.length; i++) {
            if (isTrivialEliminationByI(team, i)) {
                continue;
            }
            for (int j = i + 1; j < against[i].length; j++) {
                if (i != j && i != id(team) && j != id(team)) {
                    network.addEdge(new FlowEdge(S, game, against[i][j]));
                    network.addEdge(new FlowEdge(game, i, against[i][j]));
                    network.addEdge(new FlowEdge(game, j, against[i][j]));
                    totalNumberOfGamesBetweenTeams += against[i][j];
                    game++;
                }
            }
            if (i != id(team)) {
                network.addEdge(new FlowEdge(i, T, wins[id(team)] + remaining[id(team)] - wins[i]));
            }
        }
        FordFulkerson maxFlow = new FordFulkerson(network, S, T);
        // if all edge from S are full then the team still has a chance to be a leader (maxflow == total number of games)
        boolean isEliminated = maxFlow.value() != totalNumberOfGamesBetweenTeams;
        return new Elimination(isEliminated, maxFlow);
    }

    private boolean isTrivialElimination(String team) {
        for (int i = 0; i < teams.length; i++) {
            if (wins[id(team)] + remaining[id(team)] < wins[i]) {
                return true;
            }
        }
        return false;
    }

    private boolean isTrivialEliminationByI(String team, int i) {
        return wins[id(team)] + remaining[id(team)] < wins[i];
    }

    private int id(String team) {
        for (int i = 0; i < teams.length; i++) {
            if (teams[i].equals(team)) {
                return i;
            }
        }
        throw new IllegalArgumentException();
    }

    private int numberOfMatches(String team) {
        int n = 0;
        for (int i = 0; i < against.length; i++) {
            for (int j = i + 1; j < against[i].length; j++) {
                // skip matches with itself and matches involving "team"
                if (i != j && i != id(team) && j != id(team)) {
                    n++;
                }
            }
        }
        return n;
    }

    private void validate(String team) {
        if (team == null) {
            throw new IllegalArgumentException();
        }
        id(team);
    }

    private static class Elimination {
        private final boolean eliminated;

        private final boolean isTrivialCase;
        private final FordFulkerson maxFlow;

        public Elimination(boolean eliminated) {
            this.eliminated = eliminated;
            this.isTrivialCase = true;
            this.maxFlow = null;
        }

        public Elimination(boolean eliminated, FordFulkerson maxFlow) {
            this.eliminated = eliminated;
            this.isTrivialCase = false;
            this.maxFlow = maxFlow;
        }
    }

    public static void main(String[] args) {
        BaseballElimination division = new BaseballElimination(args[0]);
        for (String team : division.teams()) {
            if (division.isEliminated(team)) {
                StdOut.print(team + " is eliminated by the subset R = { ");
                for (String t : division.certificateOfElimination(team)) {
                    StdOut.print(t + " ");
                }
                StdOut.println("}");
            } else {
                StdOut.println(team + " is not eliminated");
            }
        }
    }
}
