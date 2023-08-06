import java.util.*;

public class Solution {
    public boolean isGood(int[] nums) {
        // 2ms
        if (nums.length < 2)
            return false;
        Arrays.sort(nums);
        int i, prev = nums[0];
        for (i = 1; i < nums.length - 1; i++) {
            if (nums[i] != prev + 1)
                return false;
            prev = nums[i];
        }
        if (nums[i] == nums.length - 1 && nums[i - 1] == nums[i])
            return true;
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = isGood(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
