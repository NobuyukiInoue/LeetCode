import java.util.*;

public class Solution {
    public int longestAlternatingSubarray(int[] nums, int threshold) {
        // 6ms - 7ms
        int ans = 0, cnt = 0, parity = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > threshold) {
                cnt = 0;
            } else if (cnt >= 1 && parity != nums[i]%2) {
                parity ^= 1;
                cnt++;
            } else {
                parity = nums[i]%2;
                cnt = parity^1;
            }
            ans = Math.max(ans, cnt);
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int threshold = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", threshold = " + threshold);
 
        long start = System.currentTimeMillis();

        int result = longestAlternatingSubarray(nums, threshold);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
