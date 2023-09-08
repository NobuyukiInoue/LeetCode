import java.util.*;

public class Solution {
    public int maxProfit(int[] prices) {
        // 2ms
		int max = 0, min = Integer.MAX_VALUE;
		for (int price : prices) {
			if (min > price) {
				min = price;
            }
			if (price - min > max) {
				max = price - min;
            }
		}
		return max;
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
