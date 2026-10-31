import java.util.*;

public class Solution {
    public int alternatingSum(int[] nums) {
        // 1ms - 2ms
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i%2 == 0) {
                ans += nums[i];
            } else {
                ans -= nums[i];
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

        int result = alternatingSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
