import java.util.*;

public class Solution {
    Mylib ml = new Mylib();

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // 0ms
        if (obstacleGrid == null)
            return 0;

        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0];

        for (int i = 1; i < n; i++) {
            if (obstacleGrid[0][i] == 0)
                obstacleGrid[0][i] = obstacleGrid[0][i - 1];
            else
                obstacleGrid[0][i] = 0;
        }

        for (int i = 1; i < m; i++) {
            if (obstacleGrid[i][0] == 0)
                obstacleGrid[i][0] = obstacleGrid[i - 1][0];
            else
                obstacleGrid[i][0] = 0;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 0)
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1];
                else
                    obstacleGrid[i][j] = 0;
            }
        }
        return obstacleGrid[m - 1][n - 1];
    }

    private void print_Grid(int[][] grid) {
        System.out.println("grid = [");
        for (int i = 0; i < grid.length; i++) {
            if (i == 0)
                System.out.println("  " + ml.intArrayToString(grid[i]));
            else
                System.out.println(", " + ml.intArrayToString(grid[i]));
        }
        System.out.println("]");
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int[][] obstacleGrid = new int[flds.length][];
            for (int i = 0; i < flds.length; i++) {
            obstacleGrid[i] = ml.stringTointArray(flds[i]);
        }

        print_Grid(obstacleGrid);

        long start = System.currentTimeMillis();
        
        int result = uniquePathsWithObstacles(obstacleGrid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
