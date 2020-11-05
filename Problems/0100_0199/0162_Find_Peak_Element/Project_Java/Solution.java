import java.util.*;

public class Solution {
    public int findPeakElement(int[] nums) {
        // 0ms
        int nums_len = nums.length;
        if (nums_len == 1 || nums_len == 0)
            return 0;
        if (nums[0] > nums[1])
            return 0;
        if (nums[nums_len - 1] > nums[nums_len - 2])
            return nums_len - 1;
        for (int i = 1; i < nums_len - 1; i++)
            if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1])
                return i;
        return 0;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = findPeakElement(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
