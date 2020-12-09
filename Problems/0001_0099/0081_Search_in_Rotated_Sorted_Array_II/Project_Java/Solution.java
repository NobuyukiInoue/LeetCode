import java.util.*;

public class Solution {
    public boolean search(int[] nums, int target) {
        // 0ms
        int left = 0;
        int right = nums.length - 1;

        while (left <=  right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return true;
            }
            if (nums[left] <= nums[mid]) {
                if (nums[left] == nums[mid] && mid != left) {
                    left++;
                    continue;
                }
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else if (nums[left] > nums[mid]) {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int target = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        boolean result = search(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
