import java.util.*;

public class Solution {
    public int minimumDeletions(int[] nums) {
        // 3ms
        int min_v = nums[0], max_v = nums[0];
        int min_p = 0, max_p = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < min_v) {
                min_v = nums[i];
                min_p = i;
            } else if (nums[i] > max_v) {
                max_v = nums[i];
                max_p = i;
            }
        }
        int left = Math.min(min_p, max_p);
        int right = Math.max(min_p, max_p);
        return Math.min(right + 1, Math.min(nums.length - left, left + 1 + (nums.length - right)));
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minimumDeletions(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
