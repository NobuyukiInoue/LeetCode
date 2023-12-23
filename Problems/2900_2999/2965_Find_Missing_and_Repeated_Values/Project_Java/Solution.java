import java.util.*;

public class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        // 1ms
        int n = grid.length;
        int[] cnts = new int[n*n + 1];
        for (int[] row : grid) {
            for (int col : row) {
                cnts[col]++;
            }
        }
        int[] ans = new int[2];
        for (int i = 1; i < cnts.length; i++) {
            if (cnts[i] == 2) {
                ans[0] = i;
            } else if (cnts[i] == 0) {
                ans[1] = i;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(str_mat);
        System.out.println("grid = " + ml.intIntArrayToString(grid));

        long start = System.currentTimeMillis();

        int[] result = findMissingAndRepeatedValues(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
