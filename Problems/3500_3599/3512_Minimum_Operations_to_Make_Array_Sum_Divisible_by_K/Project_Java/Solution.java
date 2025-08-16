import java.util.*;

public class Solution {
    public int minOperations(int[] nums, int k) {
        // 1ms
        return getArraySum(nums)%k;
    }

    private int getArraySum(int[] nums) {
        int res = 0;
        for (int num : nums) {
            res += num;
        }
        return res;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = minOperations(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
