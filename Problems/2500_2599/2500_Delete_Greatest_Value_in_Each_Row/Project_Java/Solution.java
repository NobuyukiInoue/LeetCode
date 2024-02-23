import java.util.*;

public class Solution {
    public int deleteGreatestValue(int[][] grid) {
        // 4ms
        for (int i = 0; i < grid.length; i++) {
            Arrays.sort(grid[i]);
        }
        int ans = 0;
        for (int j = grid[0].length - 1; j >= 0; j--) {
            int cur = grid[0][j];
            for (int i = 1; i < grid.length; i++) {
                cur = Math.max(cur, grid[i][j]);
            }
            ans += cur;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("grid = " + ml.intIntArrayToString(grid));

        long start = System.currentTimeMillis();

        int result = deleteGreatestValue(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
