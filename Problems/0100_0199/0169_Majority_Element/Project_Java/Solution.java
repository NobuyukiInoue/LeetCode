import java.util.*;

public class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        Mylib ml = new Mylib();

        int[] nums = ml.stringTointArray(flds);

        System.out.println("nums[] = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        Integer result = majorityElement(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
