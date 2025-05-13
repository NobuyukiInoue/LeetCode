import java.util.*;

public class Solution {
    public int subarraySum(int[] nums) {
        // 1ms
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            ans += sum_subarray(nums, Math.max(0, i - nums[i]), i);
        }
        return ans;
    }

    private int sum_subarray(int[] arr, int start, int end) {
        int v_sum = 0;
        for (int i = start; i <= end; i++) {
            v_sum += arr[i];
        }
        return v_sum;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = subarraySum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
