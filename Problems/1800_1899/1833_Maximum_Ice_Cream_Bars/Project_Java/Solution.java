import java.util.*;

public class Solution {
    public int maxIceCream(int[] costs, int coins) {
        // 38ms
        Arrays.sort(costs);
        for (int i = 0; i < costs.length; i++) {
            if ((coins -= costs[i]) < 0) {
                return i;
            }
        }
        return costs.length;
    }

    public int maxIceCream2(int[] costs, int coins) {
        // 38ms
        Arrays.sort(costs);
        int ans = 0;
        for (int cost : costs) {
            if (coins < cost)
                break;
            ans++;
            coins -= cost;
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] costs = ml.stringToIntArray(flds[0]);
        int coins = Integer.parseInt(flds[1]);
        System.out.println("costs = " + ml.intArrayToString(costs) + ", coins = " + coins);
 
        long start = System.currentTimeMillis();

        int result = maxIceCream(costs, coins);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
