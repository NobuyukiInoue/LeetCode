import java.util.*;

public class Solution {
    public int getMaximumGold(int[][] grid) {
        // 16ms
        int max = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] != 0) {
                    int count = helper(grid, i, j, 0);
                    if (count > max)
                        max = count;
                }
            }
        }
        return max;
    }

    private int helper(int[][]grid, int i, int j, int count) {
        if (grid[i][j] == 0)
            return count;
        count += grid[i][j];
        int temp = grid[i][j];
        grid[i][j] = 0;
        int[] sums = new int[4];
        if (i > 0)
            sums[0] = helper(grid, i - 1, j, count);
        if (i < grid.length - 1)
            sums[1] = helper(grid, i + 1, j, count);
        if (j > 0)
            sums[2] = helper(grid, i, j - 1, count);
        if (j < grid[i].length - 1)
            sums[3] = helper(grid, i, j + 1, count);
        grid[i][j] = temp;
        return myMax(sums);
    }

    private int myMax(int[] data) {
        int max = data[0];
        for (int i = 1; i < data.length; i++)
            if (data[i] > max)
                max = data[i];
        return max;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(flds);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        int result = getMaximumGold(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
