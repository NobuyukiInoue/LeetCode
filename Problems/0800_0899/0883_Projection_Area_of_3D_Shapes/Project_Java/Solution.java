import java.util.*;

public class Solution {
    public int projectionArea(int[][] grid) {
        int res = 0, n = grid.length;
        for (int i = 0, v = 0; i < n; ++i, res += v, v = 0)
            for (int j = 0; j < n; ++j)
                v = Math.max(v, grid[i][j]);
        for (int j = 0, v = 0; j < n; ++j, res += v, v = 0)
            for (int i = 0; i < n; ++i)
                v = Math.max(v, grid[i][j]);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (grid[i][j] > 0) res++;
        return res;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int[][] grid;

        grid = new int[flds.length][];
        Mylib ml = new Mylib();

        System.out.print("grid = [");
        for (int i = 0; i < grid.length; i++) {
            grid[i] = ml.str_to_int_array(flds[i]);
            if (i == 0)
                System.out.print(ml.output_int_array(grid[i]));
            else
                System.out.print("," + ml.output_int_array(grid[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();

        int result = projectionArea(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
