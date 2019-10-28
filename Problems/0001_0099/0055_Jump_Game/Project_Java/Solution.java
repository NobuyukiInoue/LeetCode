import java.util.*;

public class Solution {
    public boolean canJump(int[] nums) {
        // 1ms
       if (nums.length < 2)
           return true;
       
       for (int curr = nums.length - 2; curr >= 0; curr--) {
           if (nums[curr] == 0) {
               int neededJumps = 1;
               while (neededJumps > nums[curr]) {
                   neededJumps++;
                   curr--;
                   if (curr < 0)
                       return false;
               }
           }
       }
       return true;
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
        
        boolean result = canJump(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
