import java.util.*;

public class Solution {

    public int[] sortArray_default(int[] nums) {
        // 7ms
        Arrays.sort(nums);
        return nums;
    }

    public int[] sortArray(int[] nums) {
        // 3ms
        quicksort(nums, 0, nums.length - 1);
        return nums;
    }

    private int partition(int[] nums, int left, int right) {
        int pivot = nums[right];
        int start = left;
        int end = right - 1;
        int temp;
        while (start <= end) {
            if (nums[start] < pivot) {
                start++;
            } else if (nums[end] >= pivot) {
                end--;
            } else {
                temp = nums[start];
                nums[start] = nums[end];
                nums[end] = temp;
                start++;
                end--;
            }
        }
        temp = nums[start];
        nums[start] = nums[right];
        nums[right] = temp;
        return start;
    }

    private void quicksort(int[] nums, int left, int right) {
        if (left >= right)
            return;
        int pivot = partition(nums, left, right);
        quicksort(nums, left, pivot - 1);
        quicksort(nums, pivot + 1, right);
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums   = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = sortArray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
