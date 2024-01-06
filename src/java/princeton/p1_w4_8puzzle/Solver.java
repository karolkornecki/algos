import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.StdOut;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

// score 91/100
public class Solver {

    private boolean solvable = false;
    private BoardNode solution;

    // find a solution to the initial board (using the A* algorithm)
    public Solver(Board initial) {
        if (initial == null) {
            throw new IllegalArgumentException();
        }
        Board twinBoard = initial.twin();
        MinPQ<BoardNode> queue = new MinPQ<>(new BoardKeyComparator());
        MinPQ<BoardNode> twinQueue = new MinPQ<>(new BoardKeyComparator());
        queue.insert(new BoardNode(initial, 0, null));
        twinQueue.insert(new BoardNode(twinBoard, 0, null));
        while (!queue.isEmpty() || !twinQueue.isEmpty()) {
            if (!twinQueue.isEmpty()) {
                BoardNode twinBoardNode = twinQueue.delMin();
                if (twinBoardNode.board.isGoal()) {
                    solvable = false;
                    solution = null;
                    break;
                }
                for (Board neighbour : twinBoardNode.board.neighbors()) {
                    if (!visited(neighbour, twinBoardNode.previous))
                        twinQueue.insert(new BoardNode(neighbour, twinBoardNode.moves + 1, twinBoardNode));
                }
            }
            if (!queue.isEmpty()) {
                BoardNode boardNode = queue.delMin();
                if (boardNode.board.isGoal()) {
                    solvable = true;
                    solution = boardNode;
                    break;
                }
                for (Board neighbour : boardNode.board.neighbors()) {
                    if (!visited(neighbour, boardNode.previous))
                        queue.insert(new BoardNode(neighbour, boardNode.moves + 1, boardNode));
                }
            }
        }
    }

    private boolean visited(Board neighbour, BoardNode previous) {
        return previous != null && previous.board.equals(neighbour);
    }

    // is the initial board solvable? (see below)
    public boolean isSolvable() {
        return solvable;
    }

    // min number of moves to solve initial board; -1 if unsolvable
    public int moves() {
        if (!isSolvable()) {
            return -1;
        }
        return solution.moves;
    }

    // sequence of boards in a shortest solution; null if unsolvable
    public Iterable<Board> solution() {
        if (!isSolvable()) {
            return null;
        }
        BoardNode current = solution;
        List<Board> result = new ArrayList<>();
        while (current != null) {
            result.add(current.board);
            current = current.previous;
        }
        Collections.reverse(result);
        return result;
    }

    private static class BoardNode {
        private final Board board;
        private final int moves;
        private final BoardNode previous;

        public BoardNode(Board board, int moves, BoardNode previous) {
            this.board = board;
            this.moves = moves;
            this.previous = previous;
        }
    }

    private static class BoardKeyComparator implements Comparator<BoardNode> {

        @Override
        public int compare(BoardNode p, BoardNode q) {
            return Integer.compare(p.board.manhattan() + p.moves, q.board.manhattan() + q.moves);
        }
    }

    // test client (see below)
    public static void main(String[] args) {
        // create initial board from file
        In in = new In(args[0]);
        int n = in.readInt();
        int[][] tiles = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                tiles[i][j] = in.readInt();
        Board initial = new Board(tiles);

        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable()) StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }

}