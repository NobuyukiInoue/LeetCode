import java.util.*;

public class Solution {
    public boolean hasTrailingZeros(int[] nums) {
        // 1ms
        int cnt = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                if (++cnt == 2) {
                    return true;
                }
            }
        }
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = hasTrailingZeros(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
