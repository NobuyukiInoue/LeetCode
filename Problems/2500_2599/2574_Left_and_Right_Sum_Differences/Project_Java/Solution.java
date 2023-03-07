import java.util.*;

public class Solution {
    public int[] leftRigthDifference(int[] nums) {
        // 1ms
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        int left = 0, right = total;
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            left += nums[i];
            ans[i] = Math.abs(right - left);
            right -= nums[i];
        }
        return ans;
    }

    public int[] leftRigthDifference2(int[] nums) {
        // 1ms
        int n = nums.length;
        int[] ans = new int[n];
        int[] a = new int[n + 1];
        a[0] = 0;
        for (int i = 0; i < nums.length; i++) {
            a[i + 1] = a[i] + nums[i];
        }
        for (int i = 1 ; i < n + 1; i++) {
            ans[i - 1] = Math.abs(a[n] - a[i] - a[i - 1]);
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = leftRigthDifference(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
