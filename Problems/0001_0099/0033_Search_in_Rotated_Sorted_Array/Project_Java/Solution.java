import java.util.*;

public class Solution {
    public int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        while (low <= high) {
            int mid = low + ((high - low) >> 1);
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] <= nums[high]) {
                if (target > nums[mid] && target <= nums[high])
                    low = mid + 1;
                else
                    high = mid - 1;
            }
            else {
                if (target >= nums[low] && target < nums[mid])
                    high = mid - 1;
                else
                    low = mid + 1;
            }
        }
        return -1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        String[] data;
        
        int[] nums = ml.str_to_int_array(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("nums = " + ml.output_int_array(nums));
        System.out.println("target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        int result = search(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
