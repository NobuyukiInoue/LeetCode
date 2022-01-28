import java.util.*;

public class Solution {
    public int countElements(int[] nums) {
        // 1ms
        int v_max = Integer.MIN_VALUE;
        int v_min = Integer.MAX_VALUE;
        for (int num : nums) {
            v_min = Math.min(v_min, num);
            v_max = Math.max(v_max, num);
        }
        int res = 0;
        for (int num : nums) {
            if (num< v_max && num > v_min) {
                res++;
            }
        }
        return res;
    }

    public int countElements3(int[] nums) {
        // 3ms
        Arrays.sort(nums);
        int res = 0;
        for (int num : nums) {
            if (nums[0] < num && num < nums[nums.length - 1]) {
                res++;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = countElements(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
