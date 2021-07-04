import java.util.*;

public class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        // 3ms
        int total = 0;
        for (int i = 0; i < nums.length; i++) {
            total += nums[i];
            nums[i] *= 2;
        }
        if (Math.abs(total) < Math.abs(target)) {
            return 0;
        }
        target += total;
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int i = 0; i < nums.length; i++) {
            for (int j = target; j >= 0; j--) {
                if (j >= nums[i]) {
                    dp[j] += dp[j - nums[i]];
                }
            }
        }
        return dp[target];
    }

    public int findTargetSumWays2(int[] nums, int target) {
        // 488ms
        return count(nums, target, nums.length);
    }

    private int count(int[] nums, int target,int n){
        if (target == 0 && n == 0)
            return 1;
        if (n == 0)
            return 0;
        return count(nums, target + nums[n - 1], n - 1) + count(nums, target - nums[n - 1], n - 1);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int target = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        int result = findTargetSumWays(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
