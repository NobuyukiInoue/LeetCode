import java.util.*;

public class Solution {
    public int maxAscendingSum(int[] nums) {
        // 0ms
        int currentSum = nums[0], maxSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] < nums[i]) {
                currentSum += nums[i];
                if (currentSum > maxSum) {
                    maxSum = currentSum;
                }
            } else {
                currentSum = nums[i];
            }
        }
        return maxSum;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maxAscendingSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
