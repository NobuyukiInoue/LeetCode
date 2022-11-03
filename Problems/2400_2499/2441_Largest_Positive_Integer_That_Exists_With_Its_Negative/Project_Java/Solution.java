import java.util.*;

public class Solution {
    public int findMaxK(int[] nums) {
        // 5ms
        Arrays.sort(nums);
        for (int i = nums.length - 1; i >= 0; i--) {
            if (contains(nums, -nums[i])) {
                return nums[i];
            }
        }
        return -1;        
    }

    public boolean contains(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return true;
            }
            if (nums[i] > 0) {
                return false;
            }
        }
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = findMaxK(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
