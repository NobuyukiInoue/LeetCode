import java.util.*;

public class Solution {
    public int findMin(int[] nums) {
        // 0ms
        for (int i = 1; i < nums.length; i++)
            if (nums[i - 1] > nums[i])
                return nums[i];
        return nums[0];
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums) );

        long start = System.currentTimeMillis();
        
        int result = findMin(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
