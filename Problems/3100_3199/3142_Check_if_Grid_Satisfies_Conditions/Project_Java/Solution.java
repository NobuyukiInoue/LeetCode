import java.util.*;

public class Solution {
    public boolean satisfiesConditions(int[][] grid) {
        // 1ms
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j < n - 1 && grid[i][j] == grid[i][j + 1]) {
                    return false;
                }
                if (i < m - 1 && grid[i][j] != grid[i + 1][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("matrix = " + ml.intIntArrayToString(matrix));

        long start = System.currentTimeMillis();

        boolean result = satisfiesConditions(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
