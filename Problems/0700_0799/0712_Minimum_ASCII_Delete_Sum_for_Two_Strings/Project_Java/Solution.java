import java.util.*;

public class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        // 11ms
        int m = s1.length(), n = s2.length();
        char[] a = s1.toCharArray(), b = s2.toCharArray();
        int MAX = Integer.MAX_VALUE;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = m; i >= 0; i--) {
            for (int j = n; j >= 0; j--) {
                if (i < m || j < n) {
                    if (i < m && j < n && a[i] == b[j]) {
                        dp[i][j] = dp[i + 1][j + 1];
                    } else {
                        int t1, t2;
                        if (i < m)
                            t1 = a[i] + dp[i + 1][j];
                        else
                            t1 = MAX;
                        if (j < n)
                            t2 = b[j] + dp[i][j + 1];
                        else
                            t2 = MAX;
                        dp[i][j] = Math.min(t1, t2);
                    }
                }
            }
        }

        return dp[0][0];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        String s1 = flds[0];
        String s2 = flds[1];

        System.out.println("s1 = " + s1 + ", s2 = " + s2);

        long start = System.currentTimeMillis();

        int result = minimumDeleteSum(s1, s2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
