import java.util.*;

public class Solution {
    public int[][] largestLocal(int[][] grid) {
        // 3ms
        int n = grid.length;
        int[][] res = new int[n - 2][n - 2];
        for (int i = 1; i < n - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                res[i - 1][j - 1] = func(i, j, grid);
            }
        }
        return res;
    }

    public int func(int t_row, int t_col, int[][] grid){
        int maxElement = Integer.MIN_VALUE;
        for (int i = t_row - 1; i < t_row + 2; i++) {
            for (int j = t_col - 1; j < t_col + 2; j++) {
                if (grid[i][j] > maxElement) {
                    maxElement = grid[i][j];
                }
            }
        }
        return maxElement;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(str_mat);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        int[][] result = largestLocal(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
