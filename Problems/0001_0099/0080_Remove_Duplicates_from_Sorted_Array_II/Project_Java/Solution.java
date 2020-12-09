import java.util.*;

public class Solution {
    public int removeDuplicates(int[] nums) {
        // 0ms
        int numsLen = nums.length;
        if (numsLen < 3)
            return numsLen;
        int j = 0;
        for (int i = 0; i < numsLen - 2; i++) {
            if (nums[i] != nums[i + 2]) {
                nums[j++] = nums[i];
            }
        }
        nums[j++] = nums[numsLen - 2];
        nums[j++] = nums[numsLen - 1];
        return j;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = removeDuplicates(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
