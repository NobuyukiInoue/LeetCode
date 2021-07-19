import java.util.*;

public class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        // 113ms
        HashMap<Integer, Integer> cnt = new HashMap<>();
        for (int a : nums1) {
            for (int b : nums2) {
                cnt.put(a + b, cnt.getOrDefault(a + b, 0) + 1);
            }
        }

        int ans = 0;
        for (int c : nums3) {
            for (int d : nums4) {
                if (cnt.containsKey(-(c + d))) {
                    ans += cnt.get(-(c + d));
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] nums = ml.stringToIntIntArray(flds);
        int[] nums1 = nums[0], nums2 = nums[1], nums3 = nums[2], nums4 = nums[3];
        System.out.println("nums1 = " + ml.intArrayToString(nums1)
                       + ", nums2 = " + ml.intArrayToString(nums2)
                       + ", nums3 = " + ml.intArrayToString(nums3)
                       + ", nums4 = " + ml.intArrayToString(nums4));

        long start = System.currentTimeMillis();

        int result = fourSumCount(nums1, nums2, nums3, nums4);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
