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

    private void print_grid(String title, int[][] grid) {
        System.out.println(title + " = [");
        for (int i = 0; i < grid.length; i++) {
            if (i == 0)
                System.out.println("  " + ml.intArrayToString(grid[i]));
            else
                System.out.println(", " + ml.intArrayToString(grid[i]));
        }
        System.out.println("]");
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] nums = flds.split("\\],\\[");

        int[][] grid = new int[nums.length][];
            for (int i = 0; i < nums.length; i++) {
            grid[i] = ml.stringTointArray(nums[i]);
        }
        print_grid("title", grid);

        long start = System.currentTimeMillis();
        
        int result = countNegatives(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
