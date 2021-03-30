import java.util.*;

public class Solution {
    public int arrayNesting(int[] nums) {
        // 1ms
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != -1) {
                int j = i;
                int count = 0;
                while (nums[j] != -1) {
                    count++;
                    int tmp = nums[j];
                    nums[j] = -1;
                    j = tmp;
                }
                res = Math.max(res, count);
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = arrayNesting(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
