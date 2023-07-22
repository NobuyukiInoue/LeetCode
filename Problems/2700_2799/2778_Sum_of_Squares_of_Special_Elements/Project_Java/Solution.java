import java.util.*;

public class Solution {
    public int sumOfSquares(int[] nums) {
        // 1ms
        int ans = 0, n = nums.length;
        for (int i = 0; i < n; i++) {
            if (n % (i + 1) == 0) {
                ans += nums[i]*nums[i];
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

        int result = sumOfSquares(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
