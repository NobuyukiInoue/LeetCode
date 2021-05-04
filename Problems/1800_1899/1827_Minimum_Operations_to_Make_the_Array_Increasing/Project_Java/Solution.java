import java.util.*;

public class Solution {
    public int minOperations(int[] nums) {
        // 1ms
        int cnt = 0, prev = 0;
        for (int cur : nums) {
            if (cur <= prev) {
                prev++;
                cnt += prev - cur;
            } else {
                prev = cur;
            }
        }
        return cnt;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minOperations(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
