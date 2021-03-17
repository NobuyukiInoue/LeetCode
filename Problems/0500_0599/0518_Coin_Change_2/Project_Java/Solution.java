import java.util.*;

public class Solution {
    public int change(int amount, int[] coins) {
        // 2ms
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int i = 0; i < coins.length; i++) {
            for (int j = coins[i]; j < amount + 1; j++) {
                dp[j] += dp[j - coins[i]];
            }
        }
        return dp[amount];
    }

    public void Main(String temp) {
        String flds[] = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int amount = Integer.parseInt(flds[0]);
        System.out.println("amount = " + Integer.toString(amount));
        int[] coins = ml.stringToIntArray(flds[1]);
        System.out.println("coins = " + ml.intArrayToString(coins));

        long start = System.currentTimeMillis();

        int result = change(amount, coins);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
