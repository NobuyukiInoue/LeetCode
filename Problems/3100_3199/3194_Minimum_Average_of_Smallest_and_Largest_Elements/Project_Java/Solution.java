import java.util.*;

public class Solution {
    public double minimumAverage(int[] nums) {
        // 2ms
        Arrays.sort(nums);
        double ans = (nums[0] + nums[nums.length - 1])/2.0;
        for (int i = 1; i < nums.length/2 + 1; i++) {
            ans = Math.min(ans, (nums[i] + nums[nums.length - i - 1])/2.0);
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        double result = minimumAverage(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
