import java.util.*;

public class Solution {
    public int buyChoco(int[] prices, int money) {
        // 3ms
        Arrays.sort(prices);
        if (prices[0] + prices[1] <= money) {
            return money - (prices[0] + prices[1]);
        }
        return money;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] prices = ml.stringToIntArray(flds[0]);
        int money = Integer.parseInt(flds[1]);
        System.out.println("prices = " + ml.intArrayToString(prices) + ", money = " + money);
 
        long start = System.currentTimeMillis();

        int result = buyChoco(prices, money);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
