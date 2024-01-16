import java.util.*;

public class Solution {
    public int missingInteger(int[] nums) {
        // 1ms
        int total = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] + 1 == nums[i]) {
                total += nums[i];
            } else {
                break;
            }
        }
        Arrays.sort(nums);
        for (int num : nums) {
            if (num == total) {
                total++;
            }
        }
        return total;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = missingInteger(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
