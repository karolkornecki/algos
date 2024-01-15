import edu.princeton.cs.algs4.Digraph;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Topological;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class WordNet {

    private final Map<String, List<Integer>> synonymsDict = new HashMap<>();
    private final Map<Integer, List<String>> synonyms;
    private final SAP sap;

    // constructor takes the name of the two input files
    public WordNet(String s, String h) {
        validate(s);
        validate(h);
        synonyms = parseSynonyms(read(s));
        for (Integer synonymId : synonyms.keySet()) {
            for (String noun : synonyms.get(synonymId)) {
                if (synonymsDict.get(noun) == null) {
                    synonymsDict.put(noun, new ArrayList<>());
                }
                synonymsDict.get(noun).add(synonymId);
            }
        }
        // build graph
        Map<Integer, List<Integer>> hypernyms = parseHypernyms(read(h));
        Digraph digraph = new Digraph(synonyms.keySet().size());
        for (Integer v : hypernyms.keySet()) {
            for (Integer w : hypernyms.get(v)) {
                digraph.addEdge(v, w);
            }
        }
        Topological topological = new Topological(digraph);
        if (!topological.hasOrder()) {
            throw new IllegalArgumentException();
        }
        this.sap = new SAP(digraph);
    }

    private void validate(Object param) {
        if (param == null) {
            throw new IllegalArgumentException();
        }
    }

    private String[] read(String fileName) {
        return new In(fileName).readAllLines();
    }

    private Map<Integer, List<String>> parseSynonyms(String[] raw) {
        Map<Integer, List<String>> dict = new HashMap<>();
        for (String r : raw) {
            String[] a = r.split(",");
            String[] values = a[1].split(" ");
            dict.put(Integer.valueOf(a[0]), Arrays.asList(values));
        }
        return dict;
    }

    private Map<Integer, List<Integer>> parseHypernyms(String[] raw) {
        Map<Integer, List<Integer>> dict = new HashMap<>();
        for (String r : raw) {
            String[] a = r.split(",");
            List<Integer> values = new ArrayList<>();
            for (int i = 1; i < a.length; i++) {
                values.add(Integer.valueOf(a[i]));
            }
            dict.put(Integer.valueOf(a[0]), values);
        }
        return dict;
    }


    // returns all WordNet nouns
    public Iterable<String> nouns() {
        return synonymsDict.keySet();
    }

    // is the word a WordNet noun?
    public boolean isNoun(String word) {
        validate(word);
        return synonymsDict.containsKey(word);
    }

    // distance between nounA and nounB (defined below)
    public int distance(String nounA, String nounB) {
        validate(nounA);
        validate(nounB);
        isValidNoun(nounA);
        isValidNoun(nounB);
        return sap.length(synonymsDict.get(nounA), synonymsDict.get(nounB));
    }

    // a synset (second field of synsets.txt) that is the common ancestor of nounA and nounB
    // in a shortest ancestral path (defined below)
    public String sap(String nounA, String nounB) {
        validate(nounA);
        validate(nounB);
        isValidNoun(nounA);
        isValidNoun(nounB);
        int ancestor = sap.ancestor(synonymsDict.get(nounA), synonymsDict.get(nounB));
        return concat(synonyms.get(ancestor));
    }

    private String concat(List<String> nouns) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < nouns.size(); i++) {
            builder.append(nouns.get(i));
            if (i != nouns.size() - 1) {
                builder.append(" ");
            }
        }
        return builder.toString();
    }

    private void isValidNoun(String word) {
        if (!isNoun(word)) {
            throw new IllegalArgumentException();
        }
    }

    // do unit testing of this class
    public static void main(String[] args) {
    }
}