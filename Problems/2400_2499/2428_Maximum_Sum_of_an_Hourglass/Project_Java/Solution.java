import java.util.*;

public class Solution {
    public int maxSum(int[][] grid) {
        // 5ms
        int res = 0;
        for (int i = 0; i < grid.length - 2; i++) {
            for (int j = 0; j < grid[i].length - 2; j++) {
                int n_sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                          + grid[i + 1][j + 1]
                          + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2];
                res = Math.max(res, n_sum);
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(str_mat);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        int result = maxSum(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
