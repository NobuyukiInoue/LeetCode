import java.util.*;

public class Solution {
    public int maximumStrongPairXor(int[] nums) {
        // 2ms
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            for (int j = i; j < nums.length; j++) {
                int y = nums[j];
                if (Math.abs(x - y) <= Math.min(x, y)) {
                    ans = Math.max(ans, x ^ y);
                }
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

        int result = maximumStrongPairXor(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
