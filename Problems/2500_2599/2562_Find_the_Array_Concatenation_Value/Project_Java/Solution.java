import java.util.*;

public class Solution {
    public long findTheArrayConcVal(int[] nums) {
        // 3ms
        long ans = 0;
        for (int i = 0; i < nums.length/2; i++) {
            ans += Long.parseLong(Integer.toString(nums[i]) + Integer.toString(nums[nums.length - i - 1]));
        }
        if (nums.length%2 == 1) {
            ans += nums[nums.length/2];
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        long result = findTheArrayConcVal(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Long.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
