import java.util.*;

public class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        // 1ms
        int sum = 0;
        for (int num : nums)
            sum += num;
        
        if (k <= 0 || sum % k != 0)
            return false;
        
        boolean[] visited = new boolean[nums.length];
        return canPartition(nums, visited, 0, k, 0, sum/k);
    }
    
    private boolean canPartition(int[] nums, boolean[] visited, int startIndex, int k, int currentSum, int target) {
        if (k == 1)
            return true;
        if (currentSum > target)
            return false;
        if (currentSum == target)
            return canPartition(nums, visited, 0, k - 1, 0, target);
        
        for (int i = startIndex; i < nums.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                if (canPartition(nums, visited, i + 1, k, currentSum + nums[i], target)) {
                    return true;
                }
                visited[i] = false;
            }
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);

        long start = System.currentTimeMillis();

        boolean result = canPartitionKSubsets(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
