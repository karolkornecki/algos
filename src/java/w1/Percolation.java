import edu.princeton.cs.algs4.WeightedQuickUnionUF;

// Score: 94/100
public class Percolation {

    private final int n;
    private int numberOfOpened;
    private final WeightedQuickUnionUF uf;
    private final WeightedQuickUnionUF optimized;
    private final boolean[][] grid;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int nn) {
        if (nn <= 0) throw new IllegalArgumentException();
        this.n = nn;
        this.numberOfOpened = 0;
        this.uf = new WeightedQuickUnionUF(n * n);
        this.optimized = new WeightedQuickUnionUF(n * n + 2);
        for (int i = 1; i <= n; i++) { // top row
            optimized.union(0, i);
        }
        for (int i = 1; i <= n; i++) { // bottom row
            optimized.union(n * n + 1, n * n + 1 - i);
        }
        this.grid = new boolean[n][n];
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        if (isOpen(row, col)) {
            return;
        }
        row = validate(row);
        col = validate(col);
        grid[row][col] = true;
        numberOfOpened++;
        if (inRange(row - 1, col)) {
            union(row, col, row - 1, col);
        }
        if (inRange(row + 1, col)) {
            union(row, col, row + 1, col);
        }
        if (inRange(row, col + 1)) {
            union(row, col, row, col + 1);
        }
        if (inRange(row, col - 1)) {
            union(row, col, row, col - 1);
        }
    }

    private void union(int srcRow, int srcCol, int dstRow, int dstCol) {
        if (isOpen(dstRow + 1, dstCol + 1)) {
            uf.union(toIndex(srcRow, srcCol), toIndex(dstRow, dstCol));
            optimized.union(toOptimizedIndex(srcRow, srcCol), toOptimizedIndex(dstRow, dstCol));
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        row = validate(row);
        col = validate(col);
        return grid[row][col];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        if (!isOpen(row, col)) {
            return false;
        }
        row = validate(row);
        col = validate(col);
        return optimized.find(0) == optimized.find(toOptimizedIndex(row, col));
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return numberOfOpened;
    }

    // does the system percolate?
    public boolean percolates() {
        if (numberOfOpenSites() == 0) {
            return false;
        }
        return optimized.find(0) == optimized.find(n * n + 1);
    }

    private int toIndex(int row, int col) {
        return row * n + col;
    }

    private int toOptimizedIndex(int row, int col) {
        return row * n + col + 1;
    }


    private boolean inRange(int row, int col) {
        return row >= 0 && row < n && col >= 0 && col < n;
    }

    private int validate(int i) {
        if (i < 1 || i > n) {
            throw new IllegalArgumentException();
        }
        return i - 1;
    }

    // test client (optional)
    public static void main(String[] args) {

    }
}