import java.util.*;

public class Solution {
    public int numIslands(char[][] grid) {
        // 1ms
        int count = 0;
        for (int i = 0; i < grid.length; ++i) {
            for (int j = 0; j < grid[i].length; ++j) {
                if (grid[i][j] == '1') {
                    count++;
                    searchIslands(grid, i, j);
                }
            }
        }
        return count;
    }

    private void searchIslands(char[][]grid, int i, int j) {
        if (grid[i][j] == '0')
            return;
        grid[i][j] = '0';
        if (i - 1 >= 0)
            searchIslands(grid, i - 1, j);
        if (i + 1 < grid.length)
            searchIslands(grid, i + 1, j);
        if (j - 1 >= 0)
            searchIslands(grid, i, j - 1);
        if (j + 1 < grid[i].length)
            searchIslands(grid, i, j + 1);
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\",\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        char[][] grid = new char[flds.length][];
        for (int i = 0; i < flds.length; i++) {
            grid[i] = flds[i].toCharArray();
        }

        System.out.print("grid = [");
        for (int i = 0; i < grid.length; i++) {
            if (i == 0)
                System.out.print("[" + new String(grid[i]) + "]");
            else
                System.out.print(",[" + new String(grid[i]) + "]");
        }
        System.out.println("]");

        long start = System.currentTimeMillis();

        int result = numIslands(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
