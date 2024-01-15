import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class Outcast {
    private final WordNet wordNet;

    // constructor takes a WordNet object
    public Outcast(WordNet wordnet) {
        this.wordNet = wordnet;
    }

    // given an array of WordNet nouns, return an outcast
    public String outcast(String[] nouns) {
        String outcast = nouns[0];
        int max = distance(nouns, outcast);
        for (String n : nouns) {
            int d = distance(nouns, n);
            if (d > max) {
                max = d;
                outcast = n;
            }
        }
        return outcast;
    }

    private int distance(String[] nouns, String noun) {
        int d = 0;
        for (String n : nouns) {
            d += wordNet.distance(noun, n);
        }
        return d;
    }

    // see test client below
    public static void main(String[] args) {
        WordNet wordnet = new WordNet(args[0], args[1]);
        Outcast outcast = new Outcast(wordnet);
        for (int t = 2; t < args.length; t++) {
            In in = new In(args[t]);
            String[] nouns = in.readAllStrings();
            StdOut.println(args[t] + ": " + outcast.outcast(nouns));
        }
    }
}