import java.util.*;

public class Solution {
    public void wiggleSort(int[] nums) {
        // 4ms
        Arrays.sort(nums);
        for (int i = 0; i < nums.length/2; i++) {
            int temp = nums[i];
            nums[i] = nums[nums.length - 1 - i];
            nums[nums.length - 1 - i] = temp;
        }
        int [] arr = Arrays.copyOf(nums, nums.length);
        int j = 0;
        for (int i = 1; i < nums.length; i += 2) {
            nums[i] = arr[j++];
        }
        for (int i = 0; i < nums.length; i += 2) {
            nums[i] = arr[j++];
        }
    }

    public void wiggleSort2(int[] nums) {
        // 7ms
        int median = findKthLargest(nums, (nums.length + 1) / 2);
        int n = nums.length;
        int left = 0, i = 0, right = n - 1;

        while (i <= right) {
            if (nums[newIndex(i, n)] > median) {
                swap(nums, newIndex(left++, n), newIndex(i++, n));
            } else if (nums[newIndex(i, n)] < median) {
                swap(nums, newIndex(right--, n), newIndex(i, n));
            } else {
                i++;
            }
        }
    }

    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }

    private int newIndex(int index, int n) {
        return (1 + 2*index) % (n | 1);
    }

    private void swap(int[] nums, int pos1, int pos2) {
        int temp = nums[pos1];
        nums[pos1] = nums[pos2];
        nums[pos2] = temp;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        wiggleSort(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(nums));
        System.out.println((end - start)  + "ms\n");
    }
}
