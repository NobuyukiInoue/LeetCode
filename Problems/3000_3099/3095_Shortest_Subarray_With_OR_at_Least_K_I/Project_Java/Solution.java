import java.util.*;

public class Solution {
    public int minimumSubarrayLength(int[] nums, int k) {
        // 1ms
        int n = nums.length;
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int bitwise = 0;
                for (int p = i; p <= j; p++) {
                    bitwise |= nums[p];
                }
                if (bitwise >= k) {
                    res = Math.min(res, j - i + 1);
                }
            }
        }
        return res == Integer.MAX_VALUE? -1 : res;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = minimumSubarrayLength(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
