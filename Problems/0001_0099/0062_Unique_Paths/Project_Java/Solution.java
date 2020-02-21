import java.util.*;

public class Solution {
    public int uniquePaths(int m, int n) {
        // 0ms
        int[][] count = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    count[i][j] = 1;
                } else {
                    count[i][j] = count[i - 1][j] + count[i][j - 1];
                }
            }
        }

        return count[m - 1][n - 1];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        int m = Integer.parseInt(flds[0]);
        int n = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();
        
        int result = uniquePaths(m, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
