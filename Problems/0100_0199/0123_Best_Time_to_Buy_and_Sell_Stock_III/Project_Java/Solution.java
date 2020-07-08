import java.util.*;

public class Solution {
    public int maxProfit(int[] prices) {
        // 2ms
        if (prices.length <= 1) {
            return 0;
        }

        int[] start = new int[prices.length + 1];
        int[] end = new int[prices.length + 1];
        int maxp = prices[prices.length - 1];

        for (int i = prices.length - 1; i >= 0; i--) {
            if (prices[i] < maxp) {
                start[i] = Math.max(start[i + 1], maxp - prices[i]);
            } else if (prices[i] >= maxp) {
                start[i] = start[i + 1];
                maxp = prices[i];
            }
        }

        int minp = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > minp) {
                end[i] = Math.max(end[i - 1], prices[i] - minp);
            } else if (prices[i] <= minp) {
                end[i] = end[i - 1];
                minp = prices[i];
            }
        }

        int res = 0;
        for (int i = 0; i < prices.length; i++) {
            if (start[i + 1] + end[i] > res) {
                res = start[i + 1] + end[i];
            }
        }

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] prices = ml.stringTointArray(flds);
        System.out.println("prices = " + ml.intArrayToString(prices));

        long start = System.currentTimeMillis();

        int result = maxProfit(prices);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
