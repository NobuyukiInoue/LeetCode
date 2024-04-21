import java.util.*;

public class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        // 1ms
        int incr = 1, decr = 1, ans = 1;
        int prev = nums[0];
        for (int num : nums) {
            incr = num > prev? incr + 1: 1;
            decr = num < prev? decr + 1: 1;
            prev = num;
            ans = Math.max(ans, Math.max(incr, decr));
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        long result = longestMonotonicSubarray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
