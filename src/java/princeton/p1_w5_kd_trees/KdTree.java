import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.Stack;

import java.util.ArrayList;

// score 97/100
public class KdTree {
    private static final boolean VERTICAL = true;
    private static final boolean HORIZONTAL = false;
    private Node root;

    public KdTree() {
    }

    // number of points in the set
    public int size() {
        return size(root);
    }

    private int size(Node x) {
        if (x == null) return 0;
        else return x.size;
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    // add the point to the set (if it is not already in the set)
    public void insert(Point2D p) {
        validate(p);
        root = insert(root, p, VERTICAL);
    }

    private Node insert(Node x, Point2D point, boolean orientation) {
        if (x == null) return new Node(point, orientation, 1);
        if (point.equals(x.point)) {
            return x;
        }
        int cmp = orientation == VERTICAL ? Point2D.X_ORDER.compare(point, x.point) : Point2D.Y_ORDER.compare(point, x.point);
        if (cmp <= 0) {
            x.left = insert(x.left, point, !orientation);
        } else {
            x.right = insert(x.right, point, !orientation);
        }
        x.size = 1 + size(x.left) + size(x.right);
        return x;
    }

    // does the set contain point p?
    public boolean contains(Point2D p) {
        validate(p);
        return get(root, p) != null;
    }

    private Node get(Node x, Point2D point) {
        if (x == null) return null;
        if (x.point.equals(point)) {
            return x;
        }
        int cmp = x.orientation == VERTICAL ? Point2D.X_ORDER.compare(point, x.point) : Point2D.Y_ORDER.compare(point, x.point);
        if (cmp <= 0) {
            return get(x.left, point);
        } else {
            return get(x.right, point);
        }
    }

    // draw all points to standard draw
    public void draw() {
        draw(root);
    }

    private void draw(Node x) {
        if (x == null) {
            return;
        }
        x.point.draw();
        draw(x.left);
        draw(x.right);
    }

    // all points that are inside the rectangle (or on the boundary)
    public Iterable<Point2D> range(RectHV rect) {
        validate(rect);
        ArrayList<Point2D> pointsInRectangle = new ArrayList<>();
        Stack<Node> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            if (node == null) {
                continue;
            }
            if (rect.contains(node.point)) {
                pointsInRectangle.add(node.point);
                stack.push(node.left);
                stack.push(node.right);
            } else if (node.orientation == VERTICAL) {
                if (node.point.x() >= rect.xmin() && node.point.x() <= rect.xmax()) { // split the line
                    stack.push(node.left);
                    stack.push(node.right);
                } else if (node.point.x() - rect.xmin() > 0 && node.point.x() - rect.xmax() >= 0) { // rect is on the left side of the point
                    stack.push(node.left);
                } else if (rect.xmin() - node.point.x() >= 0 && rect.xmax() - node.point.x() > 0) { // rect is on the right side of the point
                    stack.push(node.right);
                }
            } else {
                if (node.point.y() >= rect.ymin() && node.point.y() <= rect.ymax()) { // split the line
                    stack.push(node.left);
                    stack.push(node.right);
                } else if (node.point.y() - rect.ymin() > 0 && node.point.y() - rect.ymax() >= 0) { // rect is below the point go left
                    stack.push(node.left);
                } else if (rect.ymin() - node.point.y() >= 0 && rect.ymax() - node.point.y() > 0) { // rect is above the point go right
                    stack.push(node.right);
                }
            }
        }
        return pointsInRectangle;
    }


    // a nearest neighbor in the set to point p; null if the set is empty
    public Point2D nearest(Point2D p) {
        validate(p);
        // TODO this one has some failing test due too amount of point visited
        Node nearest = nearest(root, p);
        return nearest != null ? nearest.point : null;
    }

    private Node nearest(Node root, Point2D target) {
        if (root == null) {
            return null;
        }
        Node highPriorityNode;
        Node lowPriorityNode;
        if ((root.orientation == VERTICAL && target.x() < root.point.x()) || (root.orientation == HORIZONTAL && target.y() < root.point.y())) {
            highPriorityNode = root.left;
            lowPriorityNode = root.right;
        } else {
            highPriorityNode = root.right;
            lowPriorityNode = root.left;
        }
        Node nearest = nearest(highPriorityNode, target);
        Node best = closest(root, nearest, target);

        double radiusSquared = best.point.distanceSquaredTo(target);
        double dist;
        if (root.orientation == VERTICAL) {
            dist = target.x() - root.point.x();
        } else {
            dist = target.y() - root.point.y();
        }

        if (radiusSquared >= dist * dist) {
            nearest = nearest(lowPriorityNode, target);
            best = closest(nearest, best, target);
        }
        return best;
    }

    private Node closest(Node node, Node maybeNearest, Point2D p) {
        if (node == null) {
            return maybeNearest;
        }
        if (maybeNearest == null) {
            return node;
        }
        if (p.distanceSquaredTo(node.point) < p.distanceSquaredTo(maybeNearest.point)) {
            return node;
        }
        return maybeNearest;
    }

    private void validate(Object param) {
        if (param == null) {
            throw new IllegalArgumentException();
        }
    }

    private static class Node {
        private final Point2D point;
        private final boolean orientation;
        private int size;
        private Node left;
        private Node right;

        public Node(Point2D point, boolean orientation, int size) {
            this.point = point;
            this.orientation = orientation;
            this.size = size;
        }
    }

    // unit testing of the methods (optional)
    public static void main(String[] args) {

    }
}