import java.util.*;

public class Solution {
    public void nextPermutation(int[] nums) {
        int p = nums.length - 1;
        while (p > 0 && nums[p] <= nums[p - 1]) {
            --p;
        }
        if (p == 0) {
            reverse(nums, 0, nums.length - 1);
            return;
        }
        int q = nums.length - 1;
        while (nums[q] <= nums[p - 1]) {
            --q;
        }
        int temp = nums[p - 1];
        nums[p - 1] = nums[q];
        nums[q] = temp;
        reverse(nums, p, nums.length - 1);
    }
    
    private void reverse(int[] a, int from, int to) {
        for (; from < to; ++from, --to) {
            int temp = a[from];
            a[from] = a[to];
            a[to] = temp;
        }
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();
        
        nextPermutation(nums);

        long end = System.currentTimeMillis();

        System.out.println("nums = " + ml.intArrayToString(nums));
        System.out.println((end - start)  + "ms\n");
    }
}
