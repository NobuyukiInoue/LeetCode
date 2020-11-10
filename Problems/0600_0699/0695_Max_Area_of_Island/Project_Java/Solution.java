import java.util.*;

public class Solution {
    private int ans;
    private int count;

    public int maxAreaOfIsland(int[][] grid) {
        // 2ms
        if (grid == null || grid[0] == null)
            return 0;
        ans = 0;
        int[][] checkTable = grid.clone();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                count = 0;
                dfs(grid, i, j, checkTable);
            }
        }
        return ans;
    }

    private void dfs(int[][] grid, int i, int j, int[][] checkTable) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[i].length)
            return;
        if (checkTable[i][j] != 1)
            return;

        checkTable[i][j] = -1;
        count += 1;

        dfs(grid, i - 1, j, checkTable);
        dfs(grid, i + 1, j, checkTable);
        dfs(grid, i, j - 1, checkTable);
        dfs(grid, i, j + 1, checkTable);

        if (count > ans)
            ans = count;

        return;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_grid = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(str_grid);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        int result = maxAreaOfIsland(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
