import java.util.*;

public class Solution {
    public int countPartitions(int[] nums) {
        // 0ms
        int sum_l = nums[0];
        for (int i = 1; i < nums.length; i++) {
            sum_l += nums[i];
        }
        int sum_r = 0;
        int ans = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            sum_l -= nums[i];
            sum_r += nums[i];
            if ((sum_l - sum_r)%2 == 0) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = countPartitions(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
