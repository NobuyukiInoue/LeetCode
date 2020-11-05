import java.util.*;

public class Solution {
    public int minPathSum(int[][] grid) {
        // 1ms
        int m = grid.length;
        int n = grid[0].length;
        int i, j;

        for (i = 1; i < n; i++)
            grid[0][i] += grid[0][i - 1];
        for (i = 1; i < m; i++)
            grid[i][0] += grid[i - 1][0];
        for (i = 1; i < m; i++)
            for (j = 1; j < n; j++)
                grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);

        return grid[m - 1][n - 1];
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] grid_str = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(grid_str);
        System.out.println("grid = " + ml.intIntArrayToString(grid));

        long start = System.currentTimeMillis();

        int result = minPathSum(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
