import java.util.*;

public class Solution {
    public int findMaxFish(int[][] grid) {
        // 4ms
        int ans = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] != 0) {
                    ans = Math.max(ans, dfs(grid, i, j, grid[i][j]));
                }
            }
        }
        return ans;
    }

    private int dfs(int[][]grid, int i, int j, int cnt) {
        grid[i][j] = 0;
        for (int[] d : new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}) {
            int ni = i + d[0], nj = j + d[1];
            if (ni < 0 || grid.length <= ni || nj < 0 || grid[0].length <= nj) {
                continue;
            }
            if (grid[ni][nj] != 0) {
                cnt += dfs(grid, ni, nj, grid[ni][nj]);
            }
        }
        return cnt;
    }

    private String gridToString(int[][] grid) {
        if (grid == null)
            return "[]";
        if (grid.length <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + "\n");
        Mylib ml = new Mylib();
        sb.append("  " + ml.intArrayToString(grid[0]) + "\n");
        for (int i = 1; i < grid.length; i++) {
            sb.append(", " + ml.intArrayToString(grid[i]) + "\n");
        }

        return sb.append("]").toString();
   }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("grid = " + gridToString(grid));

        long start = System.currentTimeMillis();

        int result = findMaxFish(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
