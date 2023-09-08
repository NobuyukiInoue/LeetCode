import java.util.*;

public class Solution {
    public int maxProfit(int[] prices) {
        // 1ms
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];
            }
        }
        return profit;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] prices = ml.stringToIntArray(flds);
        System.out.println("prices = " + ml.intArrayToString(prices));

        long start = System.currentTimeMillis();

        int result = maxProfit(prices);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
