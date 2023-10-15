import java.util.*;

public class Solution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {
        // 0ms
        int mini = 0, maxi = 0;
        for (int i = indexDifference; i< nums.length; i++) {
            if (nums[i - indexDifference] < nums[mini]) {
                mini = i - indexDifference;
            }
            if (nums[i - indexDifference] > nums[maxi]) {
                maxi = i - indexDifference;
            }
            if (nums[i] - nums[mini] >= valueDifference) {
                return new int[] {mini, i};
            }
            if (nums[maxi] - nums[i] >= valueDifference) {
                return new int[] {maxi, i};
            }
        }
        return new int[] {-1, -1};
    }

    public int[] findIndices2(int[] nums, int indexDifference, int valueDifference) {
        // 1ms
        int n = nums.length;
        for (int i = 0; i < n - indexDifference; i++) {
            for (int j = i + indexDifference; j < n; j++) {
                if (Math.abs(nums[i] - nums[j]) >= valueDifference) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {-1, -1};
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int indexDifference = Integer.parseInt(flds[1]);
        int valueDifference = Integer.parseInt(flds[2]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", indexDifference = " + indexDifference + ", valueDifference" + valueDifference);
 
        long start = System.currentTimeMillis();

        int[] result = findIndices(nums, indexDifference, valueDifference);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
