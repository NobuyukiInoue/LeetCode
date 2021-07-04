import java.util.*;

public class Solution {
    public int getMinDistance(int[] nums, int target, int start) {
        // 0ms
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] == target){
                ans = Math.min(ans, Math.abs(i - start));
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int[] flds2 = ml.stringToIntArray(flds[1]);
        int target = flds2[0];
        int start = flds2[1];
        System.out.println("nums = " + ml.intArrayToString(nums));
        System.out.println("target = " + Integer.toString(target) + ", start = " + Integer.toString(start));
        long startT = System.currentTimeMillis();

        int result = getMinDistance(nums, target, start);

        long endT = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((endT - startT)  + "ms\n");
    }
}
