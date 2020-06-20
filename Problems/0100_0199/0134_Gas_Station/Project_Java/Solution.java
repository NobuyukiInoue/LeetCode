import java.util.*;

public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // 0ms
        int start = 0, count = 0, cur = 0, n = gas.length;
    
        while (count < n && start < 2 * n) {
            cur += gas[start % n] - cost[start % n];
            if (cur < 0) {
                count = 0;
                cur = 0;
            } else {
                count++;
            }
            start++;
        }
    
        return count < n ? -1 : start % n;
    }

    public int canCompleteCircuit2(int[] gas, int[] cost) {
        // 0ms
        int n = gas.length;
        if (gas.length  < 1)
            return -1;
        
        int[] dp = new int[n];
        dp[0] = gas[0] - cost[0];

        for (int i = 1; i < n; i++) {
            dp[i] = dp[i-1] + gas[i] - cost[i];
        }

        if (dp[n - 1] >= 0) {
            int pos = min_index(dp) + 1;
            if (pos >= n)
                return 0;
            else
                return pos;
        } else {
            return -1;
        }
    }

    private int min_index(int[] nums) {
        int min_val = nums[0];
        int min_index = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < min_val) {
                min_val = nums[i];
                min_index = i;
            }
        }
        return min_index;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] gas = ml.stringTointArray(flds[0]);
        int[] cost = ml.stringTointArray(flds[1]);

        System.out.println("gas  = " + ml.intArrayToString(gas));
        System.out.println("cost = " + ml.intArrayToString(cost));

        long start = System.currentTimeMillis();
        
        int result = canCompleteCircuit(gas, cost);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
