import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.Stack;
import edu.princeton.cs.algs4.StdOut;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

// score 98/100
public class BoggleSolver {
    private final TrieST trie;

    // Initializes the data structure using the given array of strings as the dictionary.
    // (You can assume each word in the dictionary contains only the uppercase letters A through Z.)
    public BoggleSolver(String[] dictionary) {
        trie = new TrieST();
        for (String w : dictionary) {
            if (w.length() >= 3) { // exclude when length < 3 due to requirements
                trie.add(w);
            }
        }
    }

    // Returns the set of all valid words in the given Boggle board, as an Iterable.
    public Iterable<String> getAllValidWords(BoggleBoard board) {
        Set<String> words = new HashSet<>();
        for (int i = 0; i < board.rows(); i++) {
            for (int j = 0; j < board.cols(); j++) {
                Point start = new Point(i, j); // start from each possible point on board
                Stack<ProcessingWord> stack = new Stack<>();
                boolean[][] visited = new boolean[board.rows()][board.cols()];
                visited[start.row][start.col] = true;
                stack.push(new ProcessingWord(start, getLetter(start.row, start.col, board), visited));
                while (!stack.isEmpty()) {
                    ProcessingWord pw = stack.pop();
                    if (pw.word.length() >= 3 && trie.contains(pw.word)) {
                        words.add(pw.word);
                    }
                    for (Point n : neighbours(pw.point, board)) {
                        String letter = getLetter(n.row, n.col, board);
                        String prefix = pw.word + letter;
                        if (!pw.visited[n.row][n.col] && trie.containsPrefix(prefix)) {
                            boolean[][] v = clone(pw.visited);
                            v[n.row][n.col] = true;
                            stack.push(new ProcessingWord(n, prefix, v));
                        }
                    }
                }
            }
        }
        return words;
    }

    private String getLetter(int row, int col, BoggleBoard board) {
        if ('Q' == board.getLetter(row, col)) {
            return "QU";
        }
        return "" + board.getLetter(row, col);
    }

    private List<Point> neighbours(Point p, BoggleBoard board) {
        List<Point> n = new ArrayList<>();
        for (int row = p.row - 1; row <= p.row + 1; row++) {
            for (int col = p.col - 1; col <= p.col + 1; col++) {
                if (row == p.row && col == p.col) {
                    continue;
                }
                if (row >= 0 && row < board.rows() && col >= 0 && col < board.cols()) {
                    n.add(new Point(row, col));
                }
            }
        }
        return n;
    }

    // Returns the score of the given word if it is in the dictionary, zero otherwise.
    // (You can assume the word contains only the uppercase letters A through Z.)
    public int scoreOf(String word) {
        if (!trie.contains(word)) {
            return 0;
        }
        int len = word.length();
        if (len == 3 || len == 4) {
            return 1;
        } else if (len == 5) {
            return 2;
        } else if (len == 6) {
            return 3;
        } else if (len == 7) {
            return 5;
        } else if (len >= 8) {
            return 11;
        }
        throw new RuntimeException();
    }

    private boolean[][] clone(boolean[][] v) {
        boolean[][] n = new boolean[v.length][v[0].length];
        for (int i = 0; i < v.length; i++) {
            System.arraycopy(v[i], 0, n[i], 0, v[i].length);
        }
        return n;
    }

    private static class Point {
        private final int row;
        private final int col;

        public Point(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }

    private static class ProcessingWord {
        private final Point point;
        private final String word;
        private final boolean[][] visited;

        public ProcessingWord(Point point, String word, boolean[][] visited) {
            this.point = point;
            this.word = word;
            this.visited = visited;
        }

    }


    public static void main(String[] args) {
        long s = System.currentTimeMillis();
        In in = new In(args[0]);
        String[] dictionary = in.readAllStrings();
        BoggleSolver solver = new BoggleSolver(dictionary);
        BoggleBoard board = new BoggleBoard(args[1]);
        int score = 0;
        for (String word : solver.getAllValidWords(board)) {
            StdOut.println(word);
            score += solver.scoreOf(word);
        }
        StdOut.println("Score = " + score);
        long e = System.currentTimeMillis();
        System.out.println((e - s) / 1000.0 + " seconds");
    }

    private static class TrieST {
        private static final int R = 26;

        private Node root;

        private static class Node {
            private Boolean val;
            private final Node[] next = new Node[R];
        }

        public TrieST() {
        }

        public Boolean get(String key) {
            if (key == null) throw new IllegalArgumentException("argument to get() is null");
            Node x = get(root, key, 0);
            if (x == null) return null;
            return x.val;
        }

        public boolean contains(String key) {
            if (key == null) throw new IllegalArgumentException("argument to contains() is null");
            return get(key) != null;
        }

        public boolean containsPrefix(String key) {
            if (key == null) throw new IllegalArgumentException("argument to contains() is null");
            return get(root, key, 0) != null;
        }

        private Node get(Node x, String key, int d) {
            if (x == null) return null;
            if (d == key.length()) return x;
            char c = key.charAt(d);
            return get(x.next[c - 'A'], key, d + 1);
        }

        public void add(String key) {
            if (key == null) throw new IllegalArgumentException("first argument to put() is null");
            else root = add(root, key, 0);
        }

        private Node add(Node x, String key, int d) {
            if (x == null) x = new Node();
            if (d == key.length()) {
                x.val = true;
                return x;
            }
            char c = key.charAt(d);
            x.next[c - 'A'] = add(x.next[c - 'A'], key, d + 1);
            return x;
        }

        public Iterable<String> keys() {
            return keysWithPrefix("");
        }

        public Iterable<String> keysWithPrefix(String prefix) {
            Queue<String> results = new Queue<String>();
            Node x = get(root, prefix, 0);
            collect(x, new StringBuilder(prefix), results);
            return results;
        }

        private void collect(Node x, StringBuilder prefix, Queue<String> results) {
            if (x == null) return;
            if (x.val != null) results.enqueue(prefix.toString());
            for (char c = 'A'; c < 'A' + R; c++) {
                prefix.append(c);
                collect(x.next[c - 'A'], prefix, results);
                prefix.deleteCharAt(prefix.length() - 1);
            }
        }
    }
}


