import java.util.*;

public class Solution {
    public int minStartValue(int[] nums) {
        // 0ms
        int total = 0;
        int total_min = Integer.MAX_VALUE;

        for (int n : nums) {
            total += n;
            if (total < total_min) {
                total_min = total;
            }
        }

        if (-total_min + 1 > 0) {
            return -total_min + 1;
        } else {
            return 1;
        }
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minStartValue(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
