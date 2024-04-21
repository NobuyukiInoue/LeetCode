import java.util.*;

public class Solution {
    public long countAlternatingSubarrays(int[] nums) {
        // 3ms
        long ans = 1, size = 1;
        for (int i = 1; i < nums.length; i++) {
             size = nums[i - 1] == nums[i]? 1 : size + 1;
             ans += size;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        long result = countAlternatingSubarrays(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
