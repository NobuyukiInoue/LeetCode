import java.util.*;

public class Solution {
    public int findGCD(int[] nums) {
        // 1ms
        int v_min = nums[0], v_max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            v_min = Math.min(v_min, nums[i]);
            v_max = Math.max(v_max, nums[i]);
        }
        for (int i = v_min; i > 0; i--) {
            if (v_min%i == 0 && v_max%i == 0) {
                return i;
            }
        }
        return -1;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = findGCD(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
