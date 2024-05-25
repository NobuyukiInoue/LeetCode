import java.util.*;

public class Solution {
    public int addedInteger(int[] nums1, int[] nums2) {
        // 0ms
        int min1 = nums1[0], min2 = nums2[0];
        for (int i = 1; i < nums1.length; i++) {
            min1 = Math.min(min1, nums1[i]);
            min2 = Math.min(min2, nums2[i]);
        }
        return min2 - min1;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1) + ", nums2 = " + ml.intArrayToString(nums2));

        long start = System.currentTimeMillis();

        int result = addedInteger(nums1, nums2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
