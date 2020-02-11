import java.util.*;

public class Solution {
    public int coinChange(int[] coins, int amount) {
        // 7ms
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        
        for (int coin : coins) {
            for (int j = coin; j <= amount; j++) {
                if (dp[j - coin] != Integer.MAX_VALUE) {
                    dp[j] = Math.min(dp[j], dp[j - coin] + 1);
                }
            }
        }

        if (dp[amount] == Integer.MAX_VALUE)
            return -1;
        else
            return dp[amount];
    }

    public int coinChange3(int[] coins, int amount) {
        // 27ms
        if (amount < 1)
            return 0;
        return helper(coins, amount, new int[amount]);
    }
    
    private int helper(int[] coins, int rem, int[] count) {
        if (rem < 0)
            return -1;
        if (rem == 0)
            return 0;
        if (count[rem - 1] != 0)
            return count[rem - 1];

            int min = Integer.MAX_VALUE;
        for(int coin : coins) {
            int res = helper(coins, rem - coin, count);
            if (res >= 0 && res < min)
                min = 1 + res;
        }

        if (min==Integer.MAX_VALUE)
            count[rem - 1] = -1;
        else
            count[rem - 1] = min;

        return count[rem-1];
    }

    public String intArrayToString(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String flds[] = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] coins = mc.stringTointArray(flds[0]);
        System.out.println("coins = [" + intArrayToString(coins) + "]");

        int amount = Integer.parseInt(flds[1]);
        System.out.println("amount = " + Integer.toString(amount));

        long start = System.currentTimeMillis();
        
        int result = coinChange(coins, amount);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
