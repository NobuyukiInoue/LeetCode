import java.util.*;

public class Solution {
    public int maxAdjacentDistance(int[] nums) {
        // 1ms
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int next_index = (i + 1)%nums.length;
            ans = Math.max(ans, Math.abs(nums[i] - nums[next_index]));
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maxAdjacentDistance(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
