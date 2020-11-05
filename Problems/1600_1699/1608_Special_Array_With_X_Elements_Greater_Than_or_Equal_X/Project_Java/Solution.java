import java.util.*;

public class Solution {
    public int specialArray(int[] nums) {
        // 1ms
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++) {
            int n = nums.length - i;
            boolean cond1 = n <= nums[i];
            boolean cond2 = (i - 1 < 0) || (n > nums[i - 1]);
            if (cond1 && cond2)
                return n;
        }
        return -1;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = specialArray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
