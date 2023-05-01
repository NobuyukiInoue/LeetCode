import java.util.*;

public class Solution {
    public long subArrayRanges(int[] nums) {
        // 25ms - 26ms
        long res = 0;
        for (int i = 0; i < nums.length; i++) {
            int l = nums[i];
            int r = nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                l = Math.min(l, nums[j]);
                r = Math.max(r, nums[j]);
                res += r - l;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        long result = subArrayRanges(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
