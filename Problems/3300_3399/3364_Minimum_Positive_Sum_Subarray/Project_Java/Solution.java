import java.util.*;

public class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        // 3ms
        int n = nums.size();
        int min_sum = Integer.MAX_VALUE;
        for (int length = l; length <= r; length++) {
            if (length > n) {
                continue;
            }
            int window_sum = arr_sum(nums, length);
            if (window_sum > 0) {
                min_sum = Math.min(min_sum, window_sum);
            }
            for (int i = length; i < n; i++) {
                window_sum += nums.get(i) - nums.get(i - length);
                if (window_sum > 0) {
                    min_sum = Math.min(min_sum, window_sum);
                }
            }
        }
        return min_sum < Integer.MAX_VALUE? min_sum : -1;
    }

    private int arr_sum(List<Integer> nums, int length) {
        int v_sum = 0;
        for (int i = 0; i < length; i++) {
            v_sum += nums.get(i);
        }
        return v_sum;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        List<Integer> nums = ml.stringToListIntArray(flds[0]);
        int l = Integer.parseInt(flds[1]);
        int r = Integer.parseInt(flds[2]);
        System.out.println("nums = " + ml.listIntArrayToString(nums) + ", l = " + l + ", r = " + r);

        long start = System.currentTimeMillis();

        int result = minimumSumSubarray(nums, l, r);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
