import java.util.*;

public class Solution {
    public int arraySign(int[] nums) {
        // 0ms
        int isPositive = 1;
        for (int n : nums) {
            if (n == 0) {
                return 0;
            } else if (n < 0) {
                isPositive = -isPositive;
            }
        }
        return isPositive;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = arraySign(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
