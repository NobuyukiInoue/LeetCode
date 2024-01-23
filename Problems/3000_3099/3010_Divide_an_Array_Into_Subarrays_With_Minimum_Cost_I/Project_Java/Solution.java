import java.util.*;

public class Solution {
    public int minimumCost(int[] nums) {
        // 1ms
        int ans = Integer.MAX_VALUE;
        for (int i = 1; i < nums.length - 1; i++) {
            for (int j = 1; j < nums.length - i; j++) {
                ans = Math.min(ans, nums[0] + nums[i] + nums[i + j]);
            }
        }
        return ans;
    }

    public int minimumCost2(int[] nums) {
        // 3ms
        Arrays.sort(nums, 1, nums.length);
        return nums[0] + nums[1] + nums[2];
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minimumCost(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
