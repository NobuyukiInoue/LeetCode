import java.util.*;

public class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        // 1ms
        while (k > 0) {
            int n = 0;
            int v_min = Integer.MAX_VALUE;
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] < v_min) {
                    v_min = nums[i];
                    n = i;
                }
            }
            nums[n] *= multiplier;
            k--;
        }
        return nums;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        int multiplier = Integer.parseInt(flds[2]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k + ", multiplier = " + multiplier);

        long start = System.currentTimeMillis();

        int[] result = getFinalState(nums, k, multiplier);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
