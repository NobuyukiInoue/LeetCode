import java.util.*;

public class Solution {
    public int[] findBall(int[][] grid) {
        // 0ms
        int[] res = new int[grid[0].length];
        for (int i = 0; i < grid[0].length; i++) {
            res[i] = fall(i, grid);
        }
        return res;
    }

    private int fall(int pos, int[][] grid) {
        for (int j = 0; j < grid.length; j++) {
            int npos = pos + grid[j][pos];
            if (npos < 0 || npos >= grid[j].length || grid[j][npos] != grid[j][pos]) {
                return -1;
            }
            pos = npos;
        }
        return pos;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(str_mat);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        int[] result = findBall(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
