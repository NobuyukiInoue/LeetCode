import java.util.*;

public class Solution {
    public boolean canAliceWin(int[] nums) {
        // 0ms
        int s_digits = 0, d_digits = 0;
        for (int num : nums) {
            if (num < 10) {
                s_digits += num;
            } else if (num < 100) {
                d_digits += num;
            }
        }
        return (s_digits == d_digits)? false : true;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = canAliceWin(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
