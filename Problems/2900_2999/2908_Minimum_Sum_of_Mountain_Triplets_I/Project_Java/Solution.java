import java.util.*;

public class Solution {
    public int minimumSum(int[] nums) {
        // 1ms
        int ans = Integer.MAX_VALUE;
        int m = nums.length;
        for (int i = 0; i < m - 2; i++) {
            for (int j = i + 1; j <  m - 1; j++) {
                if (nums[i] < nums[j]) {
                    for (int k = j + 1; k < m; k++) {
                        if (nums[k] < nums[j]) {
                            ans = Math.min(ans, nums[i] + nums[j] + nums[k]);
                        }
                    }
                }
            }
        }
        if (ans == Integer.MAX_VALUE) {
            return -1;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minimumSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
