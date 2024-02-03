import edu.princeton.cs.algs4.BinaryStdIn;
import edu.princeton.cs.algs4.BinaryStdOut;

public class MoveToFront {

    private static final int R = 256;

    // apply move-to-front encoding, reading from standard input and writing to standard output
    public static void encode() {
        StringBuilder input = new StringBuilder();
        while (!BinaryStdIn.isEmpty()) {
            input.append(BinaryStdIn.readChar(8));
        }
        int[] ascii = new int[R];
        for (int i = 0; i < R; i++) {
            ascii[i] = i;
        }
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            int pos = 0;
            for (int j = 0; j < ascii.length; j++) {
                if (ascii[j] == c) {
                    pos = j;
                    break;
                }
            }
            BinaryStdOut.write(pos, 8);
            int j = pos;
            while (j > 0) {
                swap(j, j - 1, ascii);
                j--;
            }
        }
        BinaryStdIn.close();
        BinaryStdOut.close();
    }

    private static void swap(int x, int y, int[] a) {
        int t = a[x];
        a[x] = a[y];
        a[y] = t;
    }

    // apply move-to-front decoding, reading from standard input and writing to standard output
    public static void decode() {
        int[] ascii = new int[R];
        for (int i = 0; i < R; i++) {
            ascii[i] = i;
        }
        while (!BinaryStdIn.isEmpty()) {
            int c = BinaryStdIn.readInt(8);
            BinaryStdOut.write((char) ascii[c]);
            int j = c;
            while (j > 0) {
                swap(j, j - 1, ascii);
                j--;
            }
        }
        BinaryStdIn.close();
        BinaryStdOut.close();
    }

    // if args[0] is "-", apply move-to-front encoding
    // if args[0] is "+", apply move-to-front decoding
    public static void main(String[] args) {
        if (args[0].equals("-")) encode();
        else if (args[0].equals("+")) decode();
        else throw new IllegalArgumentException("Illegal command line argument");
    }

}