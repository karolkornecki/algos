import edu.princeton.cs.algs4.BreadthFirstDirectedPaths;
import edu.princeton.cs.algs4.Digraph;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

// score 96/100
public class SAP {

    private final Digraph g;

    // constructor takes a digraph (not necessarily a DAG)
    public SAP(Digraph G) {
        validateNotNull(G);
        g = new Digraph(G);
    }

    // length of the shortest ancestral path between v and w; -1 if no such path
    public int length(int v, int w) {
        validateVertex(v);
        validateVertex(w);
        return calculate(v, w).distance;
    }

    // a common ancestor of v and w that participates in a shortest ancestral path; -1 if no such path
    public int ancestor(int v, int w) {
        validateVertex(v);
        validateVertex(w);
        return calculate(v, w).ancestor;
    }

    // length of the shortest ancestral path between any vertex in v and any vertex in w; -1 if no such path
    public int length(Iterable<Integer> v, Iterable<Integer> w) {
        validateNotNull(v);
        validateNotNull(w);
        validateIterable(v);
        validateIterable(w);
        return calculate(v, w).distance;
    }

    // a common ancestor that participates in the shortest ancestral path; -1 if no such path
    public int ancestor(Iterable<Integer> v, Iterable<Integer> w) {
        validateNotNull(v);
        validateNotNull(w);
        validateIterable(v);
        validateIterable(w);
        return calculate(v, w).ancestor;
    }

    private Sap calculate(int v, int w) {
        int ancestor = -1;
        int distance = Integer.MAX_VALUE;
        BreadthFirstDirectedPaths bfsV = new BreadthFirstDirectedPaths(g, v);
        BreadthFirstDirectedPaths bfsW = new BreadthFirstDirectedPaths(g, w);
        for (int vertex = 0; vertex < g.V(); vertex++) {
            if (bfsV.hasPathTo(vertex) && bfsV.distTo(vertex) < distance && bfsW.hasPathTo(vertex) && bfsW.distTo(vertex) < distance) {
                int sum = bfsV.distTo(vertex) + bfsW.distTo(vertex);
                if (sum < distance) {
                    distance = sum;
                    ancestor = vertex;
                }
            }
        }
        // not found
        if (ancestor == -1) {
            distance = -1;
        }
        return new Sap(ancestor, distance);
    }

    private Sap calculate(Iterable<Integer> v, Iterable<Integer> w) {
        int ancestor = -1;
        int distance = Integer.MAX_VALUE;
        BreadthFirstDirectedPaths bfsV = new BreadthFirstDirectedPaths(g, v);
        BreadthFirstDirectedPaths bfsW = new BreadthFirstDirectedPaths(g, w);
        for (int vertex = 0; vertex < g.V(); vertex++) {
            if (bfsV.hasPathTo(vertex) && bfsV.distTo(vertex) < distance && bfsW.hasPathTo(vertex) && bfsW.distTo(vertex) < distance) {
                int sum = bfsV.distTo(vertex) + bfsW.distTo(vertex);
                if (sum < distance) {
                    distance = sum;
                    ancestor = vertex;
                }
            }
        }
        // not found
        if (ancestor == -1) {
            distance = -1;
        }
        return new Sap(ancestor, distance);
    }

    private void validateNotNull(Object param) {
        if (param == null) {
            throw new IllegalArgumentException();
        }
    }

    private void validateIterable(Iterable<Integer> iterable) {
        for (Integer vertex : iterable) {
            if (vertex == null) {
                throw new IllegalArgumentException();
            }
            validateVertex(vertex);
        }
    }

    private void validateVertex(int v) {
        if (v < 0 || v >= g.V()) {
            throw new IllegalArgumentException();
        }
    }

    private static class Sap {
        private final int ancestor;
        private final int distance;

        public Sap(int ancestor, int distance) {
            this.ancestor = ancestor;
            this.distance = distance;
        }
    }

    // do unit testing of this class
    public static void main(String[] args) {
        In in = new In(args[0]);
        Digraph G = new Digraph(in);
        SAP sap = new SAP(G);
//        List<Integer> A = new ArrayList<>();
//        A.add(13);
//        A.add(23);
//        A.add(24);
//        List<Integer> B = new ArrayList<>();
//        B.add(6);
//        B.add(16);
//        B.add(17);
//        int lengthSet = sap.length(A, B);
//        int ancestorSet = sap.ancestor(A, B);
//        StdOut.printf("lengthSet = %d, ancestorSet = %d\n", lengthSet, ancestorSet);
        while (!StdIn.isEmpty()) {
            int v = StdIn.readInt();
            int w = StdIn.readInt();
            int length = sap.length(v, w);
            int ancestor = sap.ancestor(v, w);
            StdOut.printf("length = %d, ancestor = %d\n", length, ancestor);
        }
    }
}