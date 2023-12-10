import java.util.*;

public class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        // 5ms
        int res1 = 0, res2 = 0;
        for (int num : nums1) {
            if (contains(nums2, num)) {
                res1++;
            }
        }
        for (int num : nums2) {
            if (contains(nums1, num)) {
                res2++;
            }
        }
        return new int[] {res1, res2};
    }

    private boolean contains(int[] nums, int target) {
        for (int num : nums) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1) + ", nums2 = " + ml.intArrayToString(nums2));
 
        long start = System.currentTimeMillis();

        int[] result = findIntersectionValues(nums1, nums2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
