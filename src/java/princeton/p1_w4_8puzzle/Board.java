import java.util.ArrayList;
import java.util.List;

//https://coursera.cs.princeton.edu/algs4/assignments/8puzzle/specification.php
public class Board {

    private final int[][] tiles;
    private final int[][] goal;

    private int row;
    private int col;

    private final int hamming;

    private final int manhattan;

    private final String txt;

    // create a board from an n-by-n array of tiles,
    // where tiles[row][col] = tile at (row, col)
    public Board(int[][] tiles) {
        this.tiles = tiles;
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[i].length; j++) {
                if (tiles[i][j] == 0) {
                    row = i;
                    col = j;
                    break;
                }
            }
        }
        this.goal = new int[tiles.length][tiles[0].length];
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[i].length; j++) {
                goal[i][j] = i * dimension() + j + 1;
                if (i == tiles.length - 1 && j == tiles[i].length - 1) {
                    goal[i][j] = 0;
                }
            }
        }
        this.manhattan = calculateManhattan();
        this.hamming = calculateHamming();
        this.txt = txt();
    }

    private String txt() {
        StringBuilder s = new StringBuilder(dimension() + "\n");
        for (int[] tile : tiles) {
            for (int i : tile) {
                s.append(i);
                s.append(" ");
            }
            s.append("\n");
        }
        return s.toString();
    }

    // string representation of this board
    public String toString() {
        return txt;
    }

    // board dimension n
    public int dimension() {
        return tiles.length;
    }

    // number of tiles out of place
    public int hamming() {
        return hamming;
    }

    private int calculateHamming() {
        int hammingDistance = 0;
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[i].length; j++) {
                if (tiles[i][j] != 0 && tiles[i][j] != dimension() * i + j + 1) {
                    hammingDistance++;
                }
            }
        }
        return hammingDistance;
    }

    // sum of Manhattan distances between tiles and goal
    public int manhattan() {
        return manhattan;
    }

    private int calculateManhattan() {
        int manhattanDistance = 0;
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[i].length; j++) {
                if (tiles[i][j] == 0) {
                    continue;
                }
                int[] location = findDestinationLocation(tiles[i][j]);
                manhattanDistance += Math.abs(i - location[0]) + Math.abs(j - location[1]);
            }
        }
        return manhattanDistance;
    }

    private int[] findDestinationLocation(int v) {
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[i].length; j++) {
                if (goal[i][j] == v) {
                    return new int[]{i, j};
                }
            }
        }
        throw new IllegalArgumentException();
    }

    // is this board the goal board?
    public boolean isGoal() {
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[i].length; j++) {
                if (tiles[i][j] != goal[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    // does this board equal y?
    public boolean equals(Object y) {
        if (y == null) {
            return false;
        }
        if (this == y) {
            return true;
        }
        if (y.getClass() != this.getClass()) {
            return false;
        }
        Board other = (Board) y;
        if (this.tiles.length != other.tiles.length) {
            return false;
        }
        if (this.tiles[0].length != other.tiles[0].length) {
            return false;
        }
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[i].length; j++) {
                if (tiles[i][j] != other.tiles[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    // all neighboring boards
    public Iterable<Board> neighbors() {
        int[][] neighbours = new int[][]{{row, col - 1}, {row, col + 1}, {row - 1, col}, {row + 1, col}};
        List<Board> result = new ArrayList<>();
        for (int[] n : neighbours) {
            if (n[0] >= 0 && n[0] < tiles.length && n[1] >= 0 && n[1] < tiles[0].length) {
                int[][] copy = copy();
                swap(copy, row, col, n[0], n[1]);
                result.add(new Board(copy));
            }
        }
        return result;
    }

    private void swap(int[][] copy, int srcRow, int srcCol, int destRow, int destCol) {
        int tmp = copy[srcRow][srcCol];
        copy[srcRow][srcCol] = copy[destRow][destCol];
        copy[destRow][destCol] = tmp;
    }

    private int[][] copy() {
        int[][] copy = new int[tiles.length][tiles[0].length];
        for (int i = 0; i < tiles.length; i++) {
            System.arraycopy(tiles[i], 0, copy[i], 0, tiles[i].length);
        }
        return copy;
    }

    // a board that is obtained by exchanging any pair of tiles
    public Board twin() {
        int[][] copy = copy();
        if (copy[0][0] != 0 && copy[0][1] != 0) {
            swap(copy, 0, 0, 0, 1);
        } else {
            swap(copy, 1, 0, 1, 1);
        }

        return new Board(copy);
    }

    // unit testing (not graded)
    public static void main(String[] args) {
        Board board = new Board(new int[][]{{8, 1, 3}, {4, 0, 2}, {7, 6, 5},});
        System.out.println(board);
        System.out.println(board.hamming());
        System.out.println(board.manhattan());
        System.out.println();
        for (Board n : board.neighbors()) {
            System.out.println(n);
        }
    }

}