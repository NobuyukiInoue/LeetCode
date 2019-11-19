import java.util.*;

public class Solution {
    public int closedIsland(int[][] grid) {
        // 2ms
        if (grid  == null || grid[0].length == 0)
            return 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if ((i == 0 || j == 0 || i == grid.length - 1 || j == grid[i].length - 1) && grid[i][j] == 0) {
                    dfs(grid, i, j, 1);
                }
            }
        }

        int res = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 0) {
                    dfs(grid, i, j, 1);
                    res++;
                }
            }
        }

        return res;
    }

    private void dfs(int[][] grid, int i, int j, int val) {
        if ((0 <= i && i < grid.length) && (0 <= j && j < grid[0].length) &&  grid[i][j] == 0) {
            grid[i][j] = val;
            dfs(grid, i, j + 1, val);
            dfs(grid, i + 1, j, val);
            dfs(grid, i - 1, j, val);
            dfs(grid, i, j - 1, val);
        }
    }


    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = new int[flds.length][];
            for (int i = 0; i < flds.length; i++) {
            grid[i] = ml.str_to_int_array(flds[i]);
        }

        System.out.print("grid = [");
        for (int i = 0; i < grid.length; i++) {
            if (i == 0)
                System.out.print(ml.output_int_array(grid[i]));
            else
                System.out.print("," + ml.output_int_array(grid[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        int result = closedIsland(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
