import java.util.*;

public class Solution {
    public int movesToMakeZigzag(int[] nums) {
        // 0ms
        int res[] = new int[2],  n = nums.length, left, right;
        for (int i = 0; i < n; ++i) {
            left = i > 0 ? nums[i - 1] : Integer.MAX_VALUE;
            right = i + 1 < n ? nums[i + 1] : Integer.MAX_VALUE;
            res[i % 2] += Math.max(0, nums[i] - Math.min(left, right) + 1);
        }
        return Math.min(res[0], res[1]);
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = movesToMakeZigzag(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
