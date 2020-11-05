import java.util.*;

public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        // 3ms
        int n = nums.length;
        int[] indexs = new int[n];
        for (int i = 0; i < n; i++) {
            indexs[i] = i;
        }

        quicksort(nums, indexs, 0, n - 1);
        //Arrays.sort(nums, 0, n - 1);  // Wrong Answer.
    
        for (int i = 0; i < n; i++) {
            int start = nums[i];
            int sindex = indexs[i];
            for (int j = i + 1; j < n; j++) {
                int end = nums[j];
                int eindex = indexs[j];
                long diff = (long)end - (long)start;
                if (diff > t) {
                    break;
                }
                if (Math.abs(eindex - sindex) <= k) {
                    return true;
                }
            }
        }
        return false;
    }
        
    private void quicksort(int[] nums, int[] indexs, int start, int end) {
        if (start >= end) {
            return;
        }
        int mid = start + (end - start)/2;
        int pivot = nums[mid];
        int i = start;
        int j = end;
        while (i <= j) {
            while (nums[i] < pivot) {
                i++;
            }
            while (nums[j] > pivot) {
                j--;
            }
            if (i <= j) {
                if (nums[i] != nums[j]) {
                    swap(nums, indexs, i, j);
                }
                i++;
                j--;
            }
        }
        quicksort(nums, indexs, start, i - 1);
        quicksort(nums, indexs, i, end);
    }
    
    private void swap(int[] nums, int[] indexs, int i, int j) {
        int value = nums[i];
        nums[i] = nums[j];
        nums[j] = value;
        int index = indexs[i];
        indexs[i] = indexs[j];
        indexs[j] = index;
    }

    public boolean containsNearbyAlmostDuplicate2(int[] nums, int k, int t) {
        // Wrong Answer
        if (nums == null || nums.length == 0 || k <= 0) {
            return false;
        }

        final TreeSet<Integer> values = new TreeSet<>();
        for (int ind = 0; ind < nums.length; ind++) {

            final Integer floor = values.floor(nums[ind] + t);
            final Integer ceil = values.ceiling(nums[ind] - t);
            if ((floor != null && floor >= nums[ind]) || (ceil != null && ceil <= nums[ind])) {
                return true;
            }

            values.add(nums[ind]);
            if (ind >= k) {
                values.remove(nums[ind - k]);
            }
        }

        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").trim().split("\\],");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        System.out.println("nums = " + ml.intArrayToString(nums));

        String[] fld1 = flds[1].replace("]", "").split(",");
        int k = Integer.parseInt(fld1[0]);
        int t = Integer.parseInt(fld1[1]);
        System.out.println("k = " + Integer.toString(k) + ", t = " + Integer.toString(t));

        long start = System.currentTimeMillis();

        boolean result = containsNearbyAlmostDuplicate(nums, k, t);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
