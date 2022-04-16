import java.util.*;

public class Solution {
    public int minBitFlips(int start, int goal) {
        // 0ms
        return Integer.bitCount(start ^ goal);
    }

    public int minBitFlips_loop(int start, int goal) {
        // 1ms
        int ans = 0;
        for (int x = start^goal; x > 0; x >>= 1) {
            if ((x&1) == 1) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        int start = nums[0], goal = nums[1];
        System.out.println("start = " + Integer.toString(start) + ", goal = " + Integer.toString(goal));

        long t_start = System.currentTimeMillis();

        int result = minBitFlips(start, goal);

        long t_end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((t_end - t_start)  + "ms\n");
    }
}
