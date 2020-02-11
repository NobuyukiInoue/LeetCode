import java.util.*;

public class Solution {
    public int islandPerimeter(int[][] grid) {
        int island = 0, redge = 0;
        int row = grid.length, col = grid[0].length;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    island++;
                    if (j < col - 1 && grid[i][j+1] == 1)
                        redge++;
                    if (i < row - 1 && grid[i+1][j] == 1)
                        redge++;
                }
            }
        }

        return 4*island - 2*redge;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int[][] grid;

        grid = new int[flds.length][];
        Mylib ml = new Mylib();

        System.out.print("grid = [");
        for (int i = 0; i < grid.length; i++) {
            grid[i] = ml.stringTointArray(flds[i]);
            if (i == 0)
                System.out.print(ml.intArrayToString(grid[i]));
            else
                System.out.print("," + ml.intArrayToString(grid[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();

        int result = islandPerimeter(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
