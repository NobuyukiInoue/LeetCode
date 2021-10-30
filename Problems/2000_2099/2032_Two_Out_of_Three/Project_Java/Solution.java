import java.util.*;

public class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        // 4ms
        List<Integer> list = new ArrayList<>();
        int count[][] = new int[3][101];
        for (int n : nums1)
            count[0][n] = 1;
        for (int n : nums2) 
            count[1][n] = 1;
        for (int n : nums3)
            count[2][n] = 1;
        for (int i = 1; i <= 100; i++) {
            if (count[0][i] + count[1][i] + count[2][i] > 1)
                list.add(i);
        }
        return list;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        int[] nums3 = ml.stringToIntArray(flds[2]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1) 
                       + ", nums2 = " + ml.intArrayToString(nums2)
                       + ", nums3 = " + ml.intArrayToString(nums3));

        long start = System.currentTimeMillis();

        List<Integer> result = twoOutOfThree(nums1, nums2, nums3);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
