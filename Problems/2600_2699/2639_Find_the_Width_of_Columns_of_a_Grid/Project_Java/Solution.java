import java.util.*;

public class Solution {
    public int[] findColumnWidth(int[][] grid) {
        // 7ms
        int[] ans = new int[grid[0].length];
        for (int[] row : grid) {
            for (int col = 0; col < row.length; col++) {
                ans[col] = Math.max(ans[col], Integer.toString(row[col]).length());
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(str_mat);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        int[] result = findColumnWidth(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
