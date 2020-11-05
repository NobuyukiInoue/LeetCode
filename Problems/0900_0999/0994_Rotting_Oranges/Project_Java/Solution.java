import java.util.*;

public class Solution {
    public int orangesRotting(int[][] grid) {
        int fresh = 0, d = 0;
        for (int i = 0; i < grid.length; ++i)
            for (int j = 0; j < grid[i].length; ++j)
                if (grid[i][j] == 1) ++fresh;
        for (int old_fresh = fresh; fresh > 0; ++d, old_fresh = fresh) {
            for (int i = 0; i < grid.length; ++i)
                for (int j = 0; j < grid[i].length; ++j)
                    if (grid[i][j] == d + 2)
                        fresh -= rot(grid, i + 1, j, d) + rot(grid, i - 1, j, d) + rot(grid, i, j + 1, d) + rot(grid, i, j - 1, d);
            if (fresh == old_fresh)
                return -1;
        }
        return d;
    }

    private int rot(int[][] grid, int i, int j, int d) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[i].length || grid[i][j] != 1)
            return 0;
        grid[i][j] = d + 3;
        return 1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(flds);
        System.out.print("grid = " +  ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        int result = orangesRotting(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
