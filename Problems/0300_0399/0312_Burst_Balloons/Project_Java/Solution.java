import java.util.*;

public class Solution {
    public int maxCoins(int[] nums) {
        // 5ms
        int[][] dp = new int[nums.length + 2][nums.length + 2];
        for( int k = 1; k <= nums.length;k++){
            for(int i = 0; i + k <= nums.length ;i++){
                for( int j = i + 1; j <= i + k;j++){
                    int left = i == 0 ? 1 : nums[ i - 1];
                    int right = i + k == nums.length ? 1 : nums[i + k];
                    dp[i][i+k+1] = Math.max(dp[i][i+k+1], nums[j - 1] * left * right + dp[i][j] + dp[j][i+k+1]);
                }
            }
        }
        return dp[0][nums.length + 1];
    }

    public int maxCoins2(int[] nums) {
        // 7ms
        int[] p = new int[nums.length + 2];
        System.arraycopy(nums, 0, p, 1, nums.length);
        p[0] = 1;
        p[p.length - 1] = 1;
        int n = p.length - 1;
        int[][] m = new int[n][n];
        for (int i = 0; i < n; i++)
            m[i][i] = 0;
        for (int l = 2; l <= n; l++)
            for (int i = 0; i <= n - l; i++) {
                int j = i + l - 1;
                m[i][j] = Integer.MIN_VALUE;
                for (int k = i; k < j; k++)
                    m[i][j] = Math.max(m[i][j], m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]);
            }
        return m[0][n - 1];
    }

    public int maxCoins3(int[] nums) {
        // 11ms
        if (nums == null || nums.length == 0)
            return 0;
        int[][] dp = new int[nums.length][nums.length];
        for (int len = 1; len <= nums.length; len++) {
            for (int start = 0; start <= nums.length - len; start++) {
                int end = start + len - 1;
                for (int i = start; i <= end; i++) {
                    int coins = nums[i] * getValue(nums, start - 1) * getValue(nums, end + 1);
                    coins += i != start ? dp[start][i - 1] : 0;
                    coins += i != end ? dp[i + 1][end] : 0;
                    dp[start][end] = Math.max(dp[start][end], coins);
                }
            }
        }
        return dp[0][nums.length - 1];
    }
    
    private int getValue(int[] nums, int i) {
        if (i < 0 || i >= nums.length)
            return 1;
        return nums[i];
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maxCoins(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
