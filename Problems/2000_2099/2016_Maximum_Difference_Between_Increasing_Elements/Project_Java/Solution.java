import java.util.*;

public class Solution {
    public int maximumDifference(int[] nums) {
        // 0ms
        int ans = 0;
        int prefix = nums[0];
        for (int i = 1; i < nums.length; i++) {
            ans = Math.max(ans, nums[i] - prefix);
            prefix = Math.min(prefix, nums[i]);
        }
        if (ans == 0) {
            return -1;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maximumDifference(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
