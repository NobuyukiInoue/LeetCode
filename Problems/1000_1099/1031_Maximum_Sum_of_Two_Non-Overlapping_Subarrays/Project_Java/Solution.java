import java.util.*;

public class Solution {
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        // 1ms
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        int f = firstLen, s = secondLen;
        int maxf  = nums[f-1], maxs = nums[s-1], maxt = nums[f + s - 1];
        for (int i = f + s; i < nums.length; i++) {
            maxf = Math.max(maxf, nums[i - s] - nums[i - s - f]);
            maxs = Math.max(maxs, nums[i - f] - nums[i - f - s]);
            maxt = Math.max(maxt, Math.max(maxf + nums[i] - nums[i - s], maxs + nums[i] - nums[i - f]));
        }
        return maxt;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int firstLen = Integer.parseInt(flds[1]);
        int secondLen = Integer.parseInt(flds[2]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", firstLen = " + Integer.toString(firstLen) + ", secondLen = " + Integer.toString(secondLen));

        long start = System.currentTimeMillis();

        int result = maxSumTwoNoOverlap(nums, firstLen, secondLen);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
