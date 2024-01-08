import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

import java.util.ArrayList;
import java.util.Arrays;

// score 93/100
public class FastCollinearPoints {
    private final ArrayList<SegmentNode> nodes = new ArrayList<>();
    private final ArrayList<LineSegment> segments = new ArrayList<>();

    public FastCollinearPoints(Point[] pts) {
        validate(pts);
        Point[] points = pts.clone();
        Arrays.sort(points);
        validateDuplicates(points);
        for (int p = 0; p < points.length; p++) {
            Point[] others = others(points, p);
            Arrays.sort(others, points[p].slopeOrder());
            // create list of slopes with number of points that have the same slope with point 'p'
            SlopeNode head = null;
            for (Point point : others) {
                double slope = points[p].slopeTo(point);
                if (head == null) {
                    head = new SlopeNode(slope);
                } else {
                    SlopeNode currentSlope = head.findBySlope(slope);
                    if (currentSlope == null) {
                        head.add(new SlopeNode(slope));
                    } else {
                        currentSlope.numberOfPoints++;
                    }
                }
            }
            // find only those with num >= 3
            if (head != null) {
                double[] slopes = head.filterByNumberOfPointsGte3();
                for (double slope : slopes) {
                    int count = 1;
                    for (Point other : others) {
                        double s = points[p].slopeTo(other);
                        if (s == slope) {
                            count++;
                        }
                    }
                    Point[] currentSlopePoints = new Point[count];
                    int c = 0;
                    currentSlopePoints[c++] = points[p];
                    for (Point other : others) {
                        double s = points[p].slopeTo(other);
                        if (s == slope) {
                            currentSlopePoints[c++] = other;
                        }
                    }
                    // sort arrays of points with the same slope to 'p' including 'p' point
                    Arrays.sort(currentSlopePoints);
                    // create segment([first],[last]) this is maximum segment
                    SegmentNode segmentNode = new SegmentNode(currentSlopePoints[0], currentSlopePoints[currentSlopePoints.length - 1]);
                    if (!containsSegment(segmentNode)) {
                        nodes.add(segmentNode);
                    }
                }
            }
        }
        for (SegmentNode node : nodes) {
            segments.add(new LineSegment(node.min, node.max));
        }
    }

    public int numberOfSegments() {
        return segments.size();
    }

    public LineSegment[] segments() {
        return segments.toArray(new LineSegment[0]);
    }


    private void validate(Point[] points) {
        if (points == null) {
            throw new IllegalArgumentException();
        }
        for (Point point : points) {
            if (point == null) {
                throw new IllegalArgumentException();
            }
        }
    }

    private void validateDuplicates(Point[] points) {
        for (int i = 0; i < points.length - 1; i++) {
            if (points[i].equals(points[i + 1])) {
                throw new IllegalArgumentException();
            }
        }
    }


    private static class SegmentNode {
        private final Point min;
        private final Point max;

        public SegmentNode(Point min, Point max) {
            this.min = min;
            this.max = max;
        }
    }

    private boolean containsSegment(SegmentNode segment) {
        for (SegmentNode n : nodes) {
            if (n.min.equals(segment.min) && n.max.equals(segment.max)) {
                return true;
            }
        }
        return false;
    }

    private static class SlopeNode {

        private final double slope;

        private int numberOfPoints = 1;

        private SlopeNode next;

        public SlopeNode(double slope) {
            this.slope = slope;
        }

        private void add(SlopeNode node) {
            SlopeNode current = this;
            while (current.next != null) {
                current = current.next;
            }
            current.next = node;
        }

        private SlopeNode findBySlope(double slope) {
            SlopeNode current = this;
            while (current != null) {
                if (current.slope == slope) {
                    return current;
                }
                current = current.next;
            }
            return null;
        }

        private double[] filterByNumberOfPointsGte3() {
            SlopeNode current = this;
            int count = 0;
            while (current != null) {
                if (current.numberOfPoints >= 3) {
                    count++;
                }
                current = current.next;
            }
            double[] slopes = new double[count];
            current = this;
            int i = 0;
            while (current != null) {
                if (current.numberOfPoints >= 3) {
                    slopes[i++] = current.slope;
                }
                current = current.next;
            }
            return slopes;
        }
    }

    private Point[] others(Point[] points, int p) {
        Point[] others = new Point[points.length - 1];
        int r = 0;
        for (int i = 0; i < points.length; i++) {
            if (i != p) {
                others[r++] = points[i];
            }
        }
        return others;
    }

    public static void main(String[] args) {

        // read the n points from a file
        In in = new In(args[0]);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        // draw the points
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        for (Point p : points) {
            p.draw();
        }
        StdDraw.show();

        // print and draw the line segments
        FastCollinearPoints collinear = new FastCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
        StdDraw.show();
    }
}