import java.util.*;

public class Solution {
    public int maxDistance(int[] nums1, int[] nums2) {
        // 2ms
        int res = 0, i = 0;
        for (int j = 0; j < nums2.length; ++j) {
            while (i < nums1.length && nums1[i] > nums2[j]) {
                i++;
            }
            if (i == nums1.length) {
                break;
            }
            res = Math.max(res, j - i);
        }
        return res;
    }

    public int maxDistance2(int[] nums1, int[] nums2) {
        // 2ms
        int n1 = nums1.length;
        int n2 = nums2.length;
        int maxDist = 0, j = 0;
        for (int i = 0; i < n1; i++) {
            if (j < i) {
                j = i;
            }
            while (j < n2 && nums1[i] <= nums2[j]) {
                j++;
            }
            if (j - i - 1 > maxDist) {
                maxDist = j - i - 1;
            }
            if (j == n2) {
                break;
            }
        }
        return maxDist;
    }

    public int maxDistance3(int[] nums1, int[] nums2) {
        // Time Limit Exceeded
        int ans = 0;
        for (int i = 0; i < nums1.length; i++) {
            for (int j = i; j < nums2.length; j++) {
                if (nums1[i] <= nums2[j]) {
                    ans = Math.max(ans, j - i);
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1));
        System.out.println("nums2 = " + ml.intArrayToString(nums2));

        long startT = System.currentTimeMillis();

        int result = maxDistance(nums1, nums2);

        long endT = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((endT - startT)  + "ms\n");
    }
}
