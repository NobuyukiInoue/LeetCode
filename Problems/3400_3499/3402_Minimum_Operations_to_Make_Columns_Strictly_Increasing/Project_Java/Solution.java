import java.util.*;

public class Solution {
    public int minimumOperations(int[][] grid) {
        // 1ms
        int ans = 0;
        int m = grid.length, n = grid[0].length;
        for (int col = 0; col < n; col++) {
            int cur = grid[0][col];
            for (int row = 1; row < m; row++) {
                if (grid[row][col] <= cur) {
                    ans += cur - grid[row][col] + 1;
                    cur++;
                } else {
                    cur = grid[row][col];
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("grid = " + ml.intIntArrayToString(grid));

        long start = System.currentTimeMillis();

        int result = minimumOperations(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
