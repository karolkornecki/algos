import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {

    private static final double CONFIDENCE_95 = 1.96;
    private final int[] result;
    private final int n;
    private final int t;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int gridSize, int trials) {
        if (gridSize <= 0 || trials <= 0) {
            throw new IllegalArgumentException();
        }
        this.n = gridSize;
        this.t = trials;
        this.result = new int[t];
        for (int i = 0; i < t; i++) {
            doExperiment(n, i);
        }
    }

    private void doExperiment(int gridSize, int currentNumberOfExperiment) {
        Percolation p = new Percolation(gridSize);
        while (true) {
            int row = StdRandom.uniformInt(1, gridSize + 1);
            int col = StdRandom.uniformInt(1, gridSize + 1);
            if (!p.isOpen(row, col)) {
                p.open(row, col);
                if (p.percolates()) {
                    break;
                }
            }
        }
        result[currentNumberOfExperiment] = p.numberOfOpenSites();
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(result) / (1.0 * n * n);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(result) / (1.0 * n * n);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - ((CONFIDENCE_95 * stddev()) / Math.sqrt(t));
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + ((CONFIDENCE_95 * stddev()) / Math.sqrt(t));
    }

    // test client (see below)
    public static void main(String[] args) {
        PercolationStats p = new PercolationStats(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
        System.out.println("mean                    = " + p.mean());
        System.out.println("stddev                  = " + p.stddev());
        System.out.println("95% confidence interval = [" + p.confidenceLo() + ", " + p.confidenceHi() + "]");

    }
}