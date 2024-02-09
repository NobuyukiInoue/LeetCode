import java.util.*;

public class Solution {
    public String triangleType(int[] nums) {
        // 1ms
        Arrays.sort(nums);
        if (nums[0] + nums[1] <= nums[2])
            return "none";
        else if (nums[0] == nums[1] && nums[1] == nums[2])
            return "equilateral";
        else if (nums[0] == nums[1] || nums[1] == nums[2])
            return "isosceles";
        else
            return "scalene";
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        String result = triangleType(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
