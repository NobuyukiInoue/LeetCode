import java.util.*;

public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        // 12ms
        int min = Integer.MAX_VALUE, result = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int j = i + 1;
            int k = nums.length - 1;
            while (j < k) {
                int sum =  nums[i] + nums[j] + nums[k];
                int diff = Math.abs(sum - target);
                if (diff == 0) {
                    return sum;
                }
                if (diff < min) {
                    min = diff;
                    result = sum;
                }
                if (sum <= target) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("nums = " + ml.intArrayToString(nums));
        System.out.println("target = " + String.valueOf(target));

        long start = System.currentTimeMillis();
        
        int result = threeSumClosest(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
