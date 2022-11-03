import java.util.*;

public class Solution {
    public int averageValue(int[] nums) {
        // 1ms
        int count = 0, total = 0;
        for (int num : nums) {
            if (num % 6 == 0) {
                total += num;
                count++;
            }
        }
        if (count > 0) {
            return total / count;
        }
        return 0;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = averageValue(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
