import java.util.*;

public class Solution {
    public int findLength(int[] A, int[] B) {
        // 35ms
        int m = A.length, n = B.length, res = 0;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (A[i - 1] == B[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    res = Math.max(res, dp[i][j]);
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds[0]);
        int[] B = ml.stringToIntArray(flds[1]);
        System.out.println("A = " + ml.intArrayToString(A));
        System.out.println("B = " + ml.intArrayToString(B));

        long start = System.currentTimeMillis();

        int result = findLength(A, B);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
