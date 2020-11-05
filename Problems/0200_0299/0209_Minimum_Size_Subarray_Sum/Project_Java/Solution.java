import java.util.*;

public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        // 1ms
        int i = 0, n = nums.length, res = n + 1;
        for (int j = 0; j < n; ++j) {
            s -= nums[j];
            while (s <= 0) {
                res = Math.min(res, j - i + 1);
                s += nums[i++];
            }
        }
        return res % (n + 1);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int s = Integer.parseInt(flds[0]);
        Mylib ml = new Mylib();
        int[] nums;
        
        if (flds.length > 1)
            nums = ml.stringToIntArray(flds[1]);
        else
            nums = new int[0];

        System.out.println("s = " + Integer.toString(s) + ", nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minSubArrayLen(s, nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
