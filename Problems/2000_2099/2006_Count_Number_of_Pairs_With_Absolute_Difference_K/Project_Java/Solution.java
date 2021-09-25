import java.util.*;

public class Solution {
    public int countKDifference(int[] nums, int k) {
        // 3ms
        int pairs = 0;
        int i, n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (i = 0; i < n; i++) {
            pairs += map.getOrDefault(nums[i] + k, 0);
            pairs += map.getOrDefault(nums[i] - k, 0);
            map.put(nums[i], 1 + map.getOrDefault(nums[i], 0));
        }
        return pairs;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = countKDifference(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
