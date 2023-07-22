import java.util.*;

public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // 0ms
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[[", "").replace("]]]", "").trim().split("\\]\\],\\[\\[");
        String[] flds1 = flds[0].split("\\],\\[");
        String[] flds2 = flds[1].split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds1[0]);
        int m = Integer.parseInt(flds1[1]);
        int[] nums2 = ml.stringToIntArray(flds2[0]);
        int n = Integer.parseInt(flds2[1]);

        System.out.println("nums1 = " + ml.intArrayToString(nums1) + ", m = " + m);
        System.out.println("nums2 = " + ml.intArrayToString(nums2) + ", m = " + n);

        long start = System.currentTimeMillis();
        
        merge(nums1, m, nums2, n);

        long end = System.currentTimeMillis();

        System.out.println("==== result ====");
        System.out.println("nums1 = " + ml.intArrayToString(nums1));
        System.out.println("nums2 = " + ml.intArrayToString(nums2));
        System.out.println((end - start)  + "ms\n");
    }
}
