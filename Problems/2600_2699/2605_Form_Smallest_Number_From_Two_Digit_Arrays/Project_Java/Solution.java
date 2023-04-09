import java.util.*;

public class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
        // 1ms
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        for (int n : nums1) {
            if (Contains(nums2, n)) {
                return n;
            }
        }
        if (nums1[0] < nums2[0]) {
            return 10*nums1[0] + nums2[0];
        }
        return 10*nums2[0] + nums1[0];
    }

    private boolean Contains(int[] nums, int target) {
        for (int n : nums) {
            if (n == target) {
                return true;
            }
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1) + ", nums2 = " + ml.intArrayToString(nums2));

        long start = System.currentTimeMillis();

        int result = minNumber(nums1, nums2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
