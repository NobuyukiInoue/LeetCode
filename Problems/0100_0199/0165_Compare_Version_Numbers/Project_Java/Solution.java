import java.util.*;

public class Solution {
    public int compareVersion(String version1, String version2) {
        // 1ms
        String[] str1 = version1.split("\\.");
        String[] str2 = version2.split("\\.");

        int[] nums1 = new int[str1.length];
        for (int i = 0; i < nums1.length; i++)
            nums1[i] = Integer.parseInt(str1[i]);

        int[] nums2 = new int[str2.length];
        for (int i = 0; i < nums2.length; i++)
            nums2[i] = Integer.parseInt(str2[i]);

        int v1, v2;
        for (int i = 0; i < Math.max(nums1.length, nums2.length); i++) {
            if (i < nums1.length)
                v1 = nums1[i];
            else
                v1 = 0;
            if (i < nums2.length)
                v2 = nums2[i];
            else
                v2 = 0;
            if (v1 > v2)
                return 1;
            else if (v1 < v2)
                return -1;
        }
        return 0;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String version1 = flds[0];
        String version2 = flds[1];
        System.out.println("version1 = " + version1 + ", version2 = " + version2);

        long start = System.currentTimeMillis();

        int result = compareVersion(version1, version2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
