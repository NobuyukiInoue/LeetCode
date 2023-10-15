import java.util.*;

public class Solution {
    public long maximumTripletValue(int[] nums) {
        // 1ms
        long res = 0, maxa = 0, maxab = 0;
        for (int num : nums) {
            res = Math.max(res, 1L * maxab * num);
            maxab = Math.max(maxab, maxa - num);
            maxa = Math.max(maxa, num);
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        long result = maximumTripletValue(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
