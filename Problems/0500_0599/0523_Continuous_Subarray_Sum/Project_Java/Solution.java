import java.util.*;

public class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        // 14ms
        // ArrayList<Integer> dp = new ArrayList<>();   // Time Limit Exceeded.
        Set<Integer> dp = new HashSet<>();
        int step = 0, accum = 0;
        for (int num : nums) {
            accum = (accum + num)%k;
            if (dp.contains(accum)) {
                return true;
            }
            dp.add(step);
            step = accum;
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        boolean result = checkSubarraySum(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
