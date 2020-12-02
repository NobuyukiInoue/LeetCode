import java.util.*;

public class Solution {
    public int numSubarrayprodLessThanK(int[] nums, int k) {
        // 7ms
        if (nums.length == 0 || k <= 1) {
            return 0;
        }

        int count = 0;
        int prod = 1;
        int left = 0;
        int right = 0;

        while (right < nums.length) {
            prod *= nums[right];

            while (left <= right && prod >= k) {
                prod /= nums[left];
                left++;
            }
            count += right - left + 1;
            right++;
        }

        return count;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = numSubarrayprodLessThanK(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
