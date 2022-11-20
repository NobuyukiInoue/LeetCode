import java.util.*;

public class Solution {
    public int removeDuplicates(int[] nums) {
        // 1ms - 2ms
        if (nums.length == 0) {
            return 0;
        }
        int n = 1;
    	for (int i = 1 ; i < nums.length; i++ ) {
   			if (nums[i] > nums[i - 1]) {
   				nums[n++] = nums[i];
    		}
    	}
    	return n;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = removeDuplicates(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
