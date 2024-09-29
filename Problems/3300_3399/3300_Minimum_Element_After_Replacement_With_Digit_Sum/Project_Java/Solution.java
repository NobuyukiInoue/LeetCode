import java.util.*;

public class Solution {
    public int minElement(int[] nums) {
        // 1ms
        int ans = Integer.MAX_VALUE;
        for (int num : nums) {
            int v_sum = 0;
            while (num > 0) {
                v_sum += num%10;
                num /= 10;
            }
            ans = Math.min(ans, v_sum);
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minElement(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
