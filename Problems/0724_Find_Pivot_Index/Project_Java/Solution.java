import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int pivotIndex(int[] nums) {
        if (nums.length <= 2)
            return -1;

        Integer s = 0;
        for (int i = 0; i < nums.length; i++) {
            s += nums[i];   
        }
        Integer leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (leftSum * 2 + nums[i] == s)
                return i;
            leftSum += nums[i];
        }

        return -1;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] nums = mc.str_to_int_array(flds);

        System.out.println("nums = " + mc.output_int_array(nums));

        long start = System.currentTimeMillis();
        
        int result = pivotIndex(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}