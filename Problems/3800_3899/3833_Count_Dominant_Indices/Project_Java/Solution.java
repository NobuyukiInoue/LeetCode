import java.util.*;

public class Solution {
    public int dominantIndices(int[] nums) {
        // 2ms
        int n = nums.length;
        int res = 0, total = 0;
        for (int i = 0; i < n; i++) {
            int count = i;
            int num = nums[n - 1 - i];
            if (num*count > total) 
                res++;
            total += num;
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = dominantIndices(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
