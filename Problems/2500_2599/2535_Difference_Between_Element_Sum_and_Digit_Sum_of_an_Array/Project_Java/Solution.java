import java.util.*;

public class Solution {
    public int differenceOfSum(int[] nums) {
        // 3ms
        int ele = 0, dig = 0;
        for (int num : nums) {
            ele += num;
            if (num >= 10) {
                while (num > 0) {
                    dig += num % 10;
                    num /= 10;
                }
            } else {
                dig += num;
            }
        }
        return ele - dig;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = differenceOfSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
