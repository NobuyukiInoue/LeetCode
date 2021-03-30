import java.util.*;

public class Solution {
    public int longestConsecutive(int[] nums) {
        // 2ms
        Arrays.sort(nums);
        if (nums.length == 1)
            return 1;
        int current = 1, maxIndex = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i + 1]  == nums[i] + 1) {
                current++;
            } else if (nums[i + 1] == nums[i]) {
                ;
            } else {
                current = 1;
            }
            maxIndex = Math.max(current, maxIndex);
        }
        return maxIndex;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = longestConsecutive(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
