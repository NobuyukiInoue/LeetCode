import java.util.*;

public class Solution {
    public int maxOperations(int[] nums) {
        // 0ms
        int ans = 0, total = nums[0] + nums[1];
        for (int i = 0; i < nums.length - 1; i += 2) {
            if (nums[i] + nums[i + 1] != total) {
                break;
            }
            ans++;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maxOperations(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
