import java.util.*;

public class Solution {
    public int longestNiceSubarray(int[] nums) {
        // 4ms - 13ms
        int AND = 0, i = 0, res = 0, n = nums.length;
        for (int j = 0; j < n; ++j) {
            while ((AND & nums[j]) > 0)
                AND ^= nums[i++];
            AND |= nums[j];
            res = Math.max(res, j - i + 1);
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = longestNiceSubarray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
