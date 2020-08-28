import java.util.*;

public class Solution {
    public int integerBreak(int n) {
        // 0ms
        if (n == 2)
            return 1;
        if (n == 3)
            return 2;

        int cnt2 = (3 - n % 3) % 3;
        int cnt3 = (n - cnt2 * 2) / 3;
        return (int) Math.pow(3, cnt3) * (int) Math.pow(2, cnt2);
    }

    public int integerBreak2(int n) {
        // 1ms
        int[] dp = new int[n + 1];
        dp[1] = 1;
        for (int i = 2; i <= n; i ++) {
            for (int j = 1; j < i; j ++) {
                dp[i] = Math.max(dp[i], (Math.max(j,dp[j])) * (Math.max(i - j, dp[i - j])));
            }
        }
        return dp[n];
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        int result = integerBreak(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
