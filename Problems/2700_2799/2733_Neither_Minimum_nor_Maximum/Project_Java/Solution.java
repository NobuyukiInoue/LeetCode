import java.util.*;

public class Solution {
    public int findNonMinOrMax(int[] nums) {
        // 7ms
        if (nums.length < 3) {
            return -1;
        }
        int mi = Integer.MAX_VALUE, ma = -1;
        for (int num : nums) {
            mi = Integer.min(mi, num);
            ma = Integer.max(ma, num);
        }
        for (int num : nums) {
            if (num != mi && num != ma) {
                return num;
            }
        }
        return -1;
    }

    public int findNonMinOrMax2(int[] nums) {
        // 13ms - 14ms
        if (nums.length < 3) {
            return -1;
        }
        Arrays.sort(nums);
        return nums[1];
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = findNonMinOrMax(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
