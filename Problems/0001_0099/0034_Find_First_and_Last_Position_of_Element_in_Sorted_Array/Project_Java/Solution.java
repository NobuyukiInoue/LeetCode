import java.util.*;

public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int pos = Arrays.binarySearch(nums,target);
        if (pos < 0) {
            return new int[] {-1, -1};
        }

        int left = pos;
        for (int i = left; i >= 0; i = Arrays.binarySearch(nums, 0, i, target)) {
            left = i;
        }

        int right = pos;
        for(int i = right; i >= 0; i = Arrays.binarySearch(nums, i + 1, nums.length, target)) {
            right = i;
        }
        return new int[] {left, right};
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        String[] data;

        int[] nums = ml.stringToIntArray(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("nums = " + ml.intArrayToString(nums));
        System.out.println("target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        int[] result = searchRange(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
