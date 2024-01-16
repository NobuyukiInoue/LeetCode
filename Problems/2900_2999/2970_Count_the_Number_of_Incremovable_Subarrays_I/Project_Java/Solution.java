import java.util.*;

public class Solution {
    public int incremovableSubarrayCount(int[] nums) {
        // 35ms - 37ms
        int ans = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                boolean ok = true;
                int lst = -1;
                for (int k = 0; k < n; k++) {
                    if (k >= i && k <= j) {
                        continue;
                    } else {
                        ok &= (lst < nums[k]);
                        lst = nums[k];
                    }
                }
                ans += ok ? 1 : 0;
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

        int result = incremovableSubarrayCount(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
