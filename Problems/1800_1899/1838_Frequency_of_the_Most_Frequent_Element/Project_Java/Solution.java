import java.util.*;

public class Solution {
    public int maxFrequency(int[] nums, int k) {
        // 26ms
        int res = 1, left = 0, right;
        long sum = 0;
        Arrays.sort(nums);
        for (right = 0; right < nums.length; right++) {
            sum += nums[right];
            while (sum + k < (long)nums[right] * (right - left + 1)) {
                sum -= nums[left];
                left++;
            }
            res = Math.max(res, right - left + 1);
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = maxFrequency(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
