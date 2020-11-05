import java.util.*;

public class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0)
            return 0;
        int[][] dp = new int[prices.length][2];
        dp[0][0] =- prices[0];
        dp[0][1] = 0;
        for(int i = 1; i < prices.length; i++) {
             dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] + prices[i]);
             dp[i][0] = Math.max(dp[i - 1][0], (i > 2? dp[i - 2][1]:0) - prices[i]);
        }
        return dp[prices.length - 1][1];
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();

        int[] prices = ml.stringToIntArray(flds);
        System.out.println("prices = " + ml.intArrayToString(prices));

        long start = System.currentTimeMillis();

        int result = maxProfit(prices);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
