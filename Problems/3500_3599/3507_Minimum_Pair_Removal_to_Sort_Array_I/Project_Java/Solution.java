import java.util.*;

public class Solution {
    public int minimumPairRemoval(int[] nums) {
        // 1ms
        int ans = 0;
        while (isSorted(nums)) {
            int minSum = Integer.MAX_VALUE;
            int minIdx = -1;
            for (int i = 0; i < nums.length - 1; i++) {
                if (nums[i] + nums[i + 1] < minSum) {
                    minSum = nums[i] + nums[i + 1];
                    minIdx = i;
                }
            }
            nums[minIdx] = minSum;
            nums = removeTargetIndex(nums, minIdx + 1);
            ans++;
        }
        return ans;
    }

    private boolean isSorted(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return true;
            }
        }
        return false;
    }

    private int[] removeTargetIndex(int[] nums, int target) {
        int[] res = new int[nums.length - 1];
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == target) {
                continue;
            }
            res[j++] = nums[i];
        }
        return res;
    } 

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minimumPairRemoval(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
