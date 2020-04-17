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

        Mylib ml = new Mylib();

        String[] grid_str = flds.split("\\],\\[");
        int[][] grid = new int[grid_str.length][];
    
        for (int i = 0; i < grid_str.length; i++) {
            grid[i] = ml.stringTointArray(grid_str[i]);
        }

        System.out.print("grid = [");
        for (int i = 0; i < grid.length; i++) {
            if (i == 0)
                System.out.print(ml.intArrayToString(grid[i]));
            else
                System.out.print("," + ml.intArrayToString(grid[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        int result = minPathSum(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
