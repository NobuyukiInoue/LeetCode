import java.util.*;

public class Solution {
    public boolean isArraySpecial(int[] nums) {
        // 0ms
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i]%2 == nums[i + 1]%2) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = isArraySpecial(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
