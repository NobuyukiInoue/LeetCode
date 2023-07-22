import java.util.*;

public class Solution {
    public int alternatingSubarray(int[] nums) {
        // 4ms
        int res = 0, j = 0;
        for (int i = 0; i < nums.length; i++) {
            for (j = i + 1; j < nums.length && nums[j] == nums[i] + (j - i)%2; ++j) {
                res = Math.max(res, j - i + 1);
            }
        }
        return res > 1 ? res : -1;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = alternatingSubarray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
