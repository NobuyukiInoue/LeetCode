import java.util.*;

public class Solution {
    Mylib ml = new Mylib();

    public int countNegatives(int[][] grid) {
        // 1ms
        int count = 0;
        for (int i = 0; i < grid.length; i++)
            for (int j = 0; j < grid[i].length; j++)
                if (grid[i][j] < 0)
                    count++;
        return count;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] nums = flds.split("\\],\\[");

        int[][] grid = ml.stringToIntIntArray(nums);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        int result = countNegatives(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
