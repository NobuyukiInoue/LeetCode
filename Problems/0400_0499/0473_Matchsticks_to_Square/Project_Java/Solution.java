import java.util.*;

public class Solution {
    public boolean makesquare(int[] nums) {
        // 1ms
        int sum = 0;

        for (int num: nums) {
            sum += num;
        }

        if (sum == 0 || sum % 4 != 0) {
            return false;
        }

        Arrays.sort(nums);
        reverse(nums);

        int side = sum/4;
        int[] sides = {0,0,0,0};

        return dfs(sides, 0, nums, side);
    }

    public boolean dfs(int[] sides, int index, int[] nums, int side) {
        if (index == nums.length) {
            return true;
        }

        int curr = nums[index];
        for (int i = 0; i < 4; i++) {
            if (i > 0 && sides[i] == sides[i-1]) {
                continue;
            }
            if (sides[i] + curr <= side) {
                sides[i] += curr;
                if (dfs(sides, index+1, nums, side)) {
                    return true;
                }
                sides[i] -= curr;
            }
        }
        return false;
    }

    private void reverse(int[] nums) {
        int i = 0, j = nums.length - 1;
        while (i < j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }

    public boolean makesquare2(int[] nums) {
        // 1043ms
        if (nums == null || nums.length < 4)
            return false;

        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        if (sum % 4 != 0)
            return false;

        return dfs2(nums, new int[4], 0, sum / 4);
    }

    private boolean dfs2(int[] nums, int[] sums, int index, int target) {
        if (index == nums.length) {
            if (sums[0] == target && sums[1] == target && sums[2] == target) {
                return true;
            }
            return false;
        }

        for (int i = 0; i < 4; i++) {
            if (sums[i] + nums[index] > target)
                continue;
            sums[i] += nums[index];
            if (dfs2(nums, sums, index + 1, target))
                return true;
            sums[i] -= nums[index];
        }

        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = makesquare(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
