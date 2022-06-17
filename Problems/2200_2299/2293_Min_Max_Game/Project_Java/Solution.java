import java.util.*;

public class Solution {
    public int minMaxGame(int[] nums) {
        // 1ms -  2ms
        while (nums.length > 1) {
            int[] arr = new int[nums.length / 2];
            for (int i = 0; i < arr.length; i++) {
                if (i % 2 == 0) {
                    arr[i] = Math.min(nums[2*i], nums[2*i + 1]);
                } else {
                    arr[i] = Math.max(nums[2*i], nums[2*i + 1]);
                }
            }
            nums = arr;
        }
        return nums[0];
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minMaxGame(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
