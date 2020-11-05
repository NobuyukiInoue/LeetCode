import java.util.*;

public class Solution {
    public int combinationSum4(int[] nums, int target) {
        if (nums == null || nums.length == 0 || target < 0) {
            return 0;
        }
    	int[] combs = new int[target + 1];
    	combs[0] = 1;
    	for (int i = 1; i <= target; i++) {
    		for (int j = 0; j < nums.length; j++) {
    			if (i - nums[j] >= 0) {
    				combs[i] += combs[i - nums[j]];
    			}
    		}
    	}
    	return combs[target];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("nums = " + ml.intArrayToString(nums));
        System.out.println("target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        int result = combinationSum4(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
