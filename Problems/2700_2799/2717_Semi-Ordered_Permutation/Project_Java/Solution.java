import java.util.*;

public class Solution {
    public int semiOrderedPermutation(int[] nums) {
        // 2ms
        int pos1 = 0, pos2 = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                pos1 = i;
            } else if (nums[i] == nums.length) {
                pos2 = i;
            }
        }
        return pos1 + nums.length - 1 - pos2 - (pos1 > pos2 ? 1 : 0);
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = semiOrderedPermutation(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
