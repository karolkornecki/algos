import edu.princeton.cs.algs4.BinaryStdIn;
import edu.princeton.cs.algs4.BinaryStdOut;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;

// score 99/100
public class BurrowsWheeler {

    // apply Burrows-Wheeler transform,
    // reading from standard input and writing to standard output 
    public static void transform() {
        String s = BinaryStdIn.readString();
        CircularSuffixArray csa = new CircularSuffixArray(s);
        char[] transform = new char[s.length()];
        int first = 0;
        for (int i = 0; i < s.length(); i++) {
            transform[i] = s.charAt((s.length() - 1 + csa.index(i)) % s.length());
            if (csa.index(i) == 0) { // we need to find original permutation in sorted array
                first = i;
            }
        }
        BinaryStdOut.write(first);
        for (char c : transform) {
            BinaryStdOut.write(c, 8);
        }
        BinaryStdIn.close();
        BinaryStdOut.close();
    }

    // apply Burrows-Wheeler inverse transform,
    // reading from standard input and writing to standard output
    public static void inverseTransform() {
        // TODO improve performance of this method to get 100% score
        int first = BinaryStdIn.readInt();
        String transform = BinaryStdIn.readString();
        char[] firstColumn = transform.toCharArray();
        Arrays.sort(firstColumn);
        HashMap<Character, List<Integer>> dict = new HashMap<>();
        for (int i = 0; i < transform.length(); i++) {
            if (!dict.containsKey(transform.charAt(i))) {
                dict.put(transform.charAt(i), new ArrayList<>());
            }
            dict.get(transform.charAt(i)).add(i);
        }

        HashMap<Character, Iterator<Integer>> iterDict = new HashMap<>();
        for (Character k : dict.keySet()) {
            iterDict.put(k, dict.get(k).iterator());
        }

        int[] next = new int[transform.length()];

        for (int i = 0; i < next.length; i++) {
            char ch = firstColumn[i];
            next[i] = iterDict.get(ch).next();
        }

        int current = first;
        int count = 0;
        while (count < transform.length()) {
            BinaryStdOut.write(firstColumn[current], 8);
            current = next[current];
            count++;
        }
        BinaryStdIn.close();
        BinaryStdOut.close();
    }

    // if args[0] is "-", apply Burrows-Wheeler transform
    // if args[0] is "+", apply Burrows-Wheeler inverse transform
    public static void main(String[] args) {
        if (args[0].equals("-")) transform();
        else if (args[0].equals("+")) inverseTransform();
        else throw new IllegalArgumentException("Illegal command line argument");
    }

}