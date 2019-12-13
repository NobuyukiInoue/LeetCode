import java.util.*;

public class Solution {
    public int jump(int[] nums) {
        // 1ms
        int end = 0;
        int furthest = 0;
        int result = 0;
        
        for (int i = 0; i < nums.length - 1; i++) {
            furthest = Math.max(furthest, i + nums[i]);
            if (i == end){
                result += 1;
                end = furthest;
            }
        }

        return result;
    }

    public int jump2(int[] nums) {
        // 2ms
        int n = nums.length;
        int start = 0, end = 0, step = 0;
        while (end < n - 1) {
            step++;
            int maxend = end + 1;
            for (int i = start; i < end + 1; i++) {
                if (i + nums[i] >= n - 1)
                    return step;
                maxend = Math.max(maxend, i + nums[i]);
            }
            start = end + 1;
            end = maxend;
        }

        return step;
    }

    public String intArrayToString(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";
            result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.str_to_int_array(flds);
        System.out.println("nums = " + intArrayToString(nums));

        long start = System.currentTimeMillis();
        
        int result = jump(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
