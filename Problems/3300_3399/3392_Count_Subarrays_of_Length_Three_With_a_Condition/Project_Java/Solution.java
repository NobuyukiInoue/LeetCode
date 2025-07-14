import java.util.*;

public class Solution {
    public int countSubarrays(int[] nums) {
        // 1ms
        int ans = 0;
        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i + 1] == (nums[i] + nums[i + 2])*2) {
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

        int result = countSubarrays(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
