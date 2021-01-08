import java.util.*;

public class Solution {
    public int singleNonDuplicate(int[] nums) {
        // 0ms
        int i = 0;
        while (i < nums.length - 1) {
            if (nums[i] != nums[i + 1]) {
                return nums[i];
            }
            i += 2;
        }
        return nums[i];
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums   = ml.stringToIntArray(flds);
        System.out.println("nums   = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = singleNonDuplicate(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
