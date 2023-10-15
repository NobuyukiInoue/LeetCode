import java.util.*;

public class Solution {
    public int minimumRightShifts(List<Integer> nums) {
        // 1ms
        int ind = 0, pos = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums.get(i - 1) > nums.get(i)) { 
                 ind = i;
                 pos++;
            }
        }
        if (pos > 1) {
            return -1;
        }
        if (ind == 0){
            return 0;
        }
        return nums.get(nums.size() - 1) > nums.get(0) ? -1 : nums.size() - ind; 
    }

     public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        List<Integer> nums = ml.stringToListIntArray(flds);
        System.out.println("nums = " + ml.listIntArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minimumRightShifts(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
