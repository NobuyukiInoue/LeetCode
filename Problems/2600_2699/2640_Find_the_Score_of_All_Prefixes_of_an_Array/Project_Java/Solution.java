import java.util.*;

public class Solution {
    public long[] findPrefixScore(int[] nums) {
        // 3ms - 4ms
        long[] ans = new long[nums.length + 1];
        long t_max = 0;
        for (int i = 0; i < nums.length; i++) {
            t_max = Math.max(t_max, nums[i]);
            ans[i + 1] = nums[i] + t_max + ans[i];
        }
        return Arrays.copyOfRange(ans, 1, ans.length);
    }

    private String longArrayToString(long[] nums) {
        if (nums == null)
            return "[]";
        if (nums.length <= 0)
            return "[]";

        StringBuilder resultStr = new StringBuilder("[" + Long.toString(nums[0]));
        for (int i = 1; i < nums.length; ++i)
            resultStr.append("," + Long.toString(nums[i]));
        resultStr.append("]");

        return resultStr.toString();
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        long[] result = findPrefixScore(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + longArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
