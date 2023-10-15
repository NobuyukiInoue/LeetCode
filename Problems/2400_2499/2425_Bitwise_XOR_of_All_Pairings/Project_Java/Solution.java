import java.util.*;

public class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        // 1ms
        int x = 0, y = 0;
        for (int num1: nums1) {
            x ^= num1;
        }
        for (int num2: nums2) {
            y ^= num2;
        }
        return (nums1.length%2*y) ^ (nums2.length%2*x);
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1) + ", nums2 = " + ml.intArrayToString(nums2));

        long start = System.currentTimeMillis();

        int result = xorAllNums(nums1, nums2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
