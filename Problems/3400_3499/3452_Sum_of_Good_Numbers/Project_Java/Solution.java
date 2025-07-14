import java.util.*;

public class Solution {
    public int sumOfGoodNumbers(int[] nums, int k) {
        // 1ms
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i + k < nums.length) {
                if (nums[i] <= nums[i + k]) {
                    continue;
                }
            }
            if (0 <= i - k) {
                if (nums[i] <= nums[i - k]) {
                    continue;
                }
            }
            ans += nums[i];
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = sumOfGoodNumbers(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
