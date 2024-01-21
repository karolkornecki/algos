import edu.princeton.cs.algs4.Picture;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

// score 94/100
// hint: dijkstra could be more generalized to handle both vertical and horizontal
// or even replaced with topological sort shortest path
public class SeamCarver {

    private Picture picture;

    // create a seam carver object based on the given picture
    public SeamCarver(Picture picture) {
        validate(picture);
        this.picture = new Picture(picture);
    }

    // current picture
    public Picture picture() {
        return new Picture(picture);
    }

    // width of current picture
    public int width() {
        return picture.width();
    }

    // height of current picture
    public int height() {
        return picture.height();
    }

    // energy of pixel at column x and row y
    public double energy(int x, int y) {
        validateX(x);
        validateY(y);
        if (isBorder(x, y)) {
            return 1000.0;
        }
        return Math.sqrt(xGradient(x, y) + yGradient(x, y));
    }


    private double xGradient(int x, int y) {
        int left = picture.get(x - 1, y).getRGB();
        int right = picture.get(x + 1, y).getRGB();
        int leftRed = (left >> 16) & 0xFF;
        int leftGreen = (left >> 8) & 0xFF;
        int leftBlue = left & 0xFF;
        int rightRed = (right >> 16) & 0xFF;
        int rightGreen = (right >> 8) & 0xFF;
        int rightBlue = right & 0xFF;
        return squared(leftRed - rightRed) + squared(leftGreen - rightGreen) + squared(leftBlue - rightBlue);
    }

    private double yGradient(int x, int y) {
        int top = picture.get(x, y - 1).getRGB();
        int bottom = picture.get(x, y + 1).getRGB();
        int topRed = (top >> 16) & 0xFF;
        int topGreen = (top >> 8) & 0xFF;
        int topBlue = top & 0xFF;
        int bottomRed = (bottom >> 16) & 0xFF;
        int bottomGreen = (bottom >> 8) & 0xFF;
        int bottomBlue = bottom & 0xFF;
        return squared(topRed - bottomRed) + squared(topGreen - bottomGreen) + squared(topBlue - bottomBlue);
    }

    private double squared(int x) {
        return Math.pow(x, 2);
    }

    private boolean isBorder(int x, int y) {
        return x == 0 || x == width() - 1 || y == 0 || y == height() - 1;
    }

    // sequence of indices for horizontal seam
    public int[] findHorizontalSeam() {
        if (picture.width() == 1) {
            return new int[]{0};
        }
        if (picture.height() == 1) {
            return new int[width()];
        }
        // y,x
        double[][] distTo = new double[height()][width()];
        for (int y = 0; y < distTo.length; y++) {
            for (int x = 0; x < distTo[y].length; x++) {
                distTo[y][x] = Integer.MAX_VALUE;
            }
        }
        // start from all left points
        PriorityQueue<Distance> pq = new PriorityQueue<>();
        for (int s = 0; s < height(); s++) {
            distTo[s][0] = energy(0, s);
            Distance d = new Distance(distTo[s][0], new Point(0, s), s);
            pq.add(d);
        }
        double minDistance = Integer.MAX_VALUE;
        Distance finalDistance = null;
        while (!pq.isEmpty()) {
            Distance dv = pq.poll();
            for (Point w : adjh(dv.point)) {
                if (distTo[w.y][w.x] > distTo[dv.point.y][dv.point.x] + energy(w.x, w.y)) {
                    // shorter path to w found
                    distTo[w.y][w.x] = distTo[dv.point.y][dv.point.x] + energy(w.x, w.y);
                    // update priority distance path through y coordinate
                    Distance distance = new Distance(distTo[w.y][w.x], w, dv.path, w.y);
                    pq.add(distance);
                    if (w.x == width() - 1 && distTo[w.y][w.x] < minDistance) {
                        minDistance = distTo[w.y][w.x];
                        finalDistance = distance;
                    }
                }
            }
        }
        assert finalDistance != null;
        return finalDistance.toPath();
    }


    // sequence of indices for vertical seam
    public int[] findVerticalSeam() {
        if (picture.width() == 1) {
            return new int[height()];
        }
        if (picture.height() == 1) {
            return new int[]{0};
        }
        // y,x
        double[][] distTo = new double[height()][width()];
        for (int y = 0; y < distTo.length; y++) {
            for (int x = 0; x < distTo[y].length; x++) {
                distTo[y][x] = Integer.MAX_VALUE;
            }
        }
        // start from all top points
        PriorityQueue<Distance> pq = new PriorityQueue<>();
        for (int s = 0; s < width(); s++) {
            distTo[0][s] = energy(s, 0);
            Distance d = new Distance(distTo[0][s], new Point(s, 0), s);
            pq.add(d);
        }
        double minDistance = Integer.MAX_VALUE;
        Distance finalDistance = null;
        while (!pq.isEmpty()) {
            Distance dv = pq.poll();
            for (Point w : adjv(dv.point)) {
                if (distTo[w.y][w.x] > distTo[dv.point.y][dv.point.x] + energy(w.x, w.y)) {
                    // shorter path to w found
                    distTo[w.y][w.x] = distTo[dv.point.y][dv.point.x] + energy(w.x, w.y);
                    // update priority distance path through x coordinate
                    Distance distance = new Distance(distTo[w.y][w.x], w, dv.path, w.x);
                    pq.add(distance);
                    if (w.y == height() - 1 && distTo[w.y][w.x] < minDistance) {
                        minDistance = distTo[w.y][w.x];
                        finalDistance = distance;
                    }
                }
            }
        }
        assert finalDistance != null;
        return finalDistance.toPath();
    }

    private List<Point> adjv(Point v) {
        if (v.y >= height() - 1) {
            return new ArrayList<>();
        }
        List<Point> adj = new ArrayList<>();
        if (v.x - 1 >= 0) {
            adj.add(new Point(v.x - 1, v.y + 1));
        }
        adj.add(new Point(v.x, v.y + 1));
        if (v.x + 1 < width()) {
            adj.add(new Point(v.x + 1, v.y + 1));
        }
        return adj;
    }

    private List<Point> adjh(Point v) {
        if (v.x >= width() - 1) {
            return new ArrayList<>();
        }
        List<Point> adj = new ArrayList<>();
        if (v.y - 1 >= 0) {
            adj.add(new Point(v.x + 1, v.y - 1));
        }
        adj.add(new Point(v.x + 1, v.y));
        if (v.y + 1 < height()) {
            adj.add(new Point(v.x + 1, v.y + 1));
        }
        return adj;
    }

    // remove horizontal seam from current picture
    public void removeHorizontalSeam(int[] seam) {
        validate(seam);
        if (seam.length != width()) {
            throw new IllegalArgumentException();
        }
        validateStep(seam);
        for (int y : seam) {
            validateY(y);
        }
        Picture p = new Picture(width(), height() - 1);
        for (int x = 0, srcX = 0; x < p.width(); x++, srcX++) {
            for (int y = 0, srcY = 0; y < p.height(); y++, srcY++) {
                if (srcY == seam[x]) {
                    srcY++;
                }
                if (srcY < picture.height()) {
                    p.setRGB(x, y, picture.getRGB(srcX, srcY));
                }
            }
        }
        picture = p;
    }

    // remove vertical seam from current picture
    public void removeVerticalSeam(int[] seam) {
        validate(seam);
        if (seam.length != height()) {
            throw new IllegalArgumentException();
        }
        validateStep(seam);
        for (int x : seam) {
            validateX(x);
        }
        Picture p = new Picture(width() - 1, height());
        for (int y = 0, srcY = 0; y < p.height(); y++, srcY++) {
            for (int x = 0, srcX = 0; x < p.width(); x++, srcX++) {
                if (srcX == seam[y]) {
                    srcX++;
                }
                if (srcX < picture.width()) {
                    p.setRGB(x, y, picture.getRGB(srcX, srcY));
                }
            }
        }
        picture = p;
    }

    private void validate(Object obj) {
        if (obj == null) {
            throw new IllegalArgumentException();
        }
    }

    private void validateStep(int[] seam) {
        for (int i = 1; i < seam.length; i++) {
            if (Math.abs(seam[i] - seam[i - 1]) > 1) {
                throw new IllegalArgumentException();
            }
        }
    }

    private void validateX(int x) {
        if (x < 0 || x > width() - 1) {
            throw new IllegalArgumentException();
        }
    }

    private void validateY(int y) {
        if (y < 0 || y > height() - 1) {
            throw new IllegalArgumentException();
        }
    }

    private static class Point {
        private final int x;
        private final int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static class Distance implements Comparable<Distance> {
        private final double distance;
        private final Point point;
        private final List<Integer> path = new ArrayList<>();

        public Distance(double distance, Point point, Integer startPath) {
            this.distance = distance;
            this.point = point;
            this.path.add(startPath);
        }

        public Distance(double distance, Point point, List<Integer> currentPath, Integer nextNodeInPath) {
            this.distance = distance;
            this.point = point;
            this.path.addAll(currentPath);
            this.path.add(nextNodeInPath);
        }

        private int[] toPath() {
            int[] a = new int[path.size()];
            for (int i = 0; i < a.length; i++) {
                a[i] = path.get(i);
            }
            return a;
        }

        @Override
        public int compareTo(Distance o) {
            return Double.compare(this.distance, o.distance);
        }
    }

    //  unit testing (optional)
    public static void main(String[] args) {
        System.out.println("Tests");
    }

}