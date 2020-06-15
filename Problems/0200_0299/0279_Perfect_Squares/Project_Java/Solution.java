import java.util.*;

public class Solution {
    public int numSquares(int n) {
        // 28ms
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 1; i <  n + 1; i++) {
            int sqi = i * i;
            for (int j = sqi; j < n + 1; j++) {
                dp[j] = Math.min(dp[j], 1 + dp[j - sqi]);
             }
        }
        return dp[n];
     }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = numSquares(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
