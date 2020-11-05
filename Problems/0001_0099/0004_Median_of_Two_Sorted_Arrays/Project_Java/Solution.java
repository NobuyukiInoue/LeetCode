import java.util.*;

public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        if (len1 == 0 && len2 == 0)
            return 0;
        int midIndex = (len1 + len2) / 2;
        int[] a = new int[len1 + len2];
        double re = 0.0;
        int index = 0;
        for (int i = 0, j = 0; i < len1 || j < len2; ) {
            if (index - 1 == midIndex)
                break;
            if (i >= len1 || (j < len2 && nums1[i] > nums2[j])) {
                a[index++] = nums2[j];
                j++;
            } else {
                a[index++] = nums1[i];
                i++;
            }
        }
        re = (len1 + len2) % 2 == 0 ? (a[midIndex] + a[midIndex - 1]) / 2.0 : a[midIndex];
        return re;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1));
        System.out.println("nums2 = " + ml.intArrayToString(nums2));

        long start = System.currentTimeMillis();

        double result = findMedianSortedArrays(nums1, nums2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Double.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
