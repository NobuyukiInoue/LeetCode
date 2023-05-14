import java.util.*;

public class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {
        // 289ms - 290ms
        int max_cnt = -1, ans = -1;
        for (int divisor : divisors) {
            int cnt = 0;
            for (int num : nums) {
                if (num % divisor == 0) {
                    cnt++;
                }
            }
            if (cnt > max_cnt) {
                max_cnt = cnt;
                ans = divisor;
            } else if (cnt == max_cnt) {
                ans = Math.min(ans, divisor);
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int[] divisors = ml.stringToIntArray(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", divisors = " + ml.intArrayToString(divisors));

        long start = System.currentTimeMillis();

        int result = maxDivScore(nums, divisors);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
