import java.util.*;

public class Solution {
    public int maxProfit(int[] prices, int fee) {
        // 3ms
        if (prices.length < 2)
             return 0;
        int ans = 0;
        int minimum = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < minimum) {
                minimum = prices[i];
            } else if (prices[i] > minimum + fee) {
                ans += prices[i] - fee - minimum;
                minimum = prices[i] - fee;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        Mylib ml = new Mylib();
        int[] prices = ml.stringToIntArray(flds[0]);
        int fee = Integer.parseInt(flds[1]);
        System.out.println("prices = " + ml.intArrayToString(prices) + ", fee = " + Integer.toString(fee));

        long start = System.currentTimeMillis();

        int result = maxProfit(prices, fee);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
