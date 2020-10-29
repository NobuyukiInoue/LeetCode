import java.util.*;

public class Solution {
    public boolean canPartition(int[] nums) {
        // 10ms
        int sum = 0;
        for (int n:nums)
            sum += n;
        if ((sum&1) == 1)
            return false;

        int v = (sum>>1);
        boolean[] dp = new boolean[v+1];
        dp[0] = true;
        for (int n:nums) {
            for (int i = v; i >= n; --i)
                dp[i] |= dp[i - n];
            if(dp[v])
                return true;
        }
        return dp[v];
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = canPartition(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
