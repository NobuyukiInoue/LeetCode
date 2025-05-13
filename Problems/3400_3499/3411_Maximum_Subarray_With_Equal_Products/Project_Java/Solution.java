import java.util.*;

public class Solution {
    public int maxLength(int[] nums) {
        // 1ms
        int n = nums.length;
        int ans = 2;
        int i, j;
        for (i = 0; i < n - 1; i++) {
            int v_gcd = nums[i];
            int v_lcm = nums[i];
            boolean is_longest = false;
            for (j = i + 1; j < n; j++) {
                v_gcd = gcd(v_gcd, nums[j]);
                if (v_gcd != 1 || gcd(v_lcm, nums[j]) != 1) {
                    ans = Math.max(ans, j - i);
                    is_longest = true;
                    break;
                }
                v_lcm *= nums[j];
            }
            if (!is_longest) {
                ans = Math.max(ans, j - i);
            }
        }
        return ans;
    }

    private int gcd (int a, int b) {
        return b == 0? a: gcd(b, a%b);
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maxLength(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
