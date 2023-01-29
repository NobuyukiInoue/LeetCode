import java.util.*;

public class Solution {
    public int maximumCount(int[] nums) {
        // 0ms - 1ms
        int pos = 0, neg = 0;
        for (int n : nums) {
            if (n > 0) {
                pos++;
            } else if (n < 0) {
                neg++;
            }
        }
        return Math.max(pos, neg);
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maximumCount(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
