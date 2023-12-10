import java.util.*;

public class Solution {
    public int smallestRangeII(int[] nums, int k) {
        // 11ms
        Arrays.sort(nums);
        int n = nums.length;
        int score = nums[n - 1] - nums[0];
        int v_min, v_max, res = score;
        for (int i = 0; i < n - 1; i++) {
            v_max = Math.max(nums[i] + k , nums[n - 1] - k);
            v_min = Math.min(nums[i + 1] - k , nums[0] + k);
            score = v_max - v_min;
            res = Math.min(res, score);
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        int result = smallestRangeII(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
