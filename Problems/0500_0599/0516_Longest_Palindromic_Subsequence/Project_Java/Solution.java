import java.util.*;

public class Solution {
    public int longestPalindromeSubseq(String s) {
        // 32ms
        int n = s.length();
        int[] dp = new int[n];
        dp[n - 1] = 1;
        for (int i = n - 1; i >= 0; i--) {
            int[] newdp = dp.clone();
            newdp[i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    newdp[j] = 2 + dp[j - 1];
                } else {
                    newdp[j] = Math.max(dp[j], newdp[j - 1]);
                }
            }
            dp = newdp;
        }
        return dp[n - 1];
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = longestPalindromeSubseq(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
