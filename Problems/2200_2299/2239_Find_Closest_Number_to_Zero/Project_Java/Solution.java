import java.util.*;

public class Solution {
    public int findClosestNumber(int[] nums) {
        // 2ms
        int[] min_v = new int[] {Math.abs(nums[0]), nums[0]};
        for(int i = 1; i < nums.length; i++) {
            if (Math.abs(nums[i]) < min_v[0]) {
                min_v[0] = Math.abs(nums[i]);
                min_v[1] = nums[i];
            } else if (Math.abs(nums[i]) == min_v[0]) {
                min_v[1] = Math.max(min_v[1], nums[i]);
            }
        }
        return min_v[1];
    }

    public int findClosestNumber2(int[] nums) {
        // 2ms
        int ans = nums[0];
        for(int i = 1; i < nums.length; i++) {
            if (Math.abs(nums[i] - 0) <= Math.abs(ans - 0)) {
                if (Math.abs(nums[i] - 0) == Math.abs(ans - 0)) {
                    ans = Math.max(ans, nums[i]);
                } else {
                    ans = nums[i];    
                }      
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = findClosestNumber(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
