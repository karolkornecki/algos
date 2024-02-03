import edu.princeton.cs.algs4.Stack;

import java.util.Arrays;

public class CircularSuffixArray {

    private final String s;
    private final int[] index;

    // circular suffix array of s
    public CircularSuffixArray(String s) {
        if (s == null) {
            throw new IllegalArgumentException();
        }
        this.s = s;
        Suffix[] suffixes = new Suffix[s.length()];
        for (int i = 0; i < s.length(); i++) {
            suffixes[i] = new Suffix(s, i);
        }
        Arrays.sort(suffixes);
        index = new int[s.length()];
        for (int i = 0; i < suffixes.length; i++) {
            index[i] = suffixes[i].start;
        }
    }

    // length of s
    public int length() {
        return s.length();
    }

    // returns index of ith sorted suffix
    public int index(int i) {
        if (i < 0 || i >= length()) {
            throw new IllegalArgumentException();
        }
        return index[i];
    }

    private static class Suffix implements Comparable<Suffix> {
        private final String str;
        private final int start;

        private Suffix(String str, int start) {
            this.str = str;
            this.start = start;
        }

        private char charAt(int i) {
            return str.charAt((start + i) % str.length());
        }

        @Override
        public int compareTo(Suffix other) {
            Stack<Integer> stack = new Stack<>();
            stack.push(0);
            int counter = 0;
            while (!stack.isEmpty() && counter < str.length()) {
                int e = stack.pop();
                if (this.charAt(e) < other.charAt(e)) {
                    return -1;
                }
                if (this.charAt(e) > other.charAt(e)) {
                    return 1;
                }
                counter++;
                if (counter == str.length()) {
                    break;
                }
                stack.push(next(e));
            }
            return 0;
        }

        private int next(int i) {
            return i + 1 % str.length();
        }
    }

    // unit testing (required)
    public static void main(String[] args) {
        CircularSuffixArray c = new CircularSuffixArray("CADABRA!ABRA");
        for (int i = 0; i < c.length(); i++) {
            System.out.println(c.index(i));
        }
        System.out.println(c.length());
    }

}