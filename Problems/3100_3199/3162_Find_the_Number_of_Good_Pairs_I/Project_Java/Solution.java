import java.util.*;

public class Solution {
    public int numberOfPairs(int[] nums1, int[] nums2, int k) {
        // 1ms
        int ans = 0;
        for (int num1 : nums1) {
            for (int num2 : nums2) {
                if (num1 % (num2*k) == 0) {
                    ans++;
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        int k = Integer.parseInt(flds[2]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1) + ", nums2 = " + ml.intArrayToString(nums2) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = numberOfPairs(nums1, nums2, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
