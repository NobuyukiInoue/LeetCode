import java.util.*;

public class Solution {
    public int findLHS(int[] nums) {
	    if (nums.length == 0) {
	        return 0;
	    }
	    Arrays.sort(nums);
	    int start = 0;
		int nextstart = 0;
		int res = 0;
	    for (int i = 1; i < nums.length; i++) {
	        if (nums[i] - nums[start] == 1) {
	            if (nums[nextstart] < nums[i]) {
	                nextstart = i;
	            }
	            res = Math.max(res, i - start + 1);
	        } else if (nums[i] - nums[start] > 1) {
	            start = start == nextstart ? i : nextstart;
	            i--;
	        }
	    }
	    return res;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);

        long start = System.currentTimeMillis();

        int result = findLHS(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
