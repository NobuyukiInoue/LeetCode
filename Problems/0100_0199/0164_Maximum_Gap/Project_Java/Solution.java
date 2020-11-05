import java.util.*;

public class Solution {
    public int maximumGap(int[] nums) {
        // 2ms
        Arrays.sort(nums);
        int max = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            int temp = nums[i + 1] - nums[i];
            if (temp > max)
                max = temp;
        }
        return max;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maximumGap(nums);

        long end = System.currentTimeMillis();

        System.out.println(String.format("result = %d", result));
        System.out.println((end - start)  + "ms\n");
    }
}
