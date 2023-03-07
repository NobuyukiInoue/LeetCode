import java.util.*;

public class Solution {
    public int maxOperations(int[] nums, int k) {
        // 19ms
        Arrays.sort(nums);
        int low = 0, high = nums.length - 1, minOperations = 0;
        while (low < high) {
            if (nums[low] + nums[high] == k) {
                low++;
                high--;
                minOperations++;
            } else if (nums[low] + nums[high] > k) {
                high--;
            } else {
                low++;
            }
        }
        return minOperations;
    }

    public int maxOperations_use_HashMap(int[] nums, int k) {
        // 38ms
        HashMap<Integer, Integer> cnts = new HashMap<>();
        for (int num : nums) {
            cnts.put(num, cnts.getOrDefault(num, 0) + 1);
        }
        int ans = 0;
        for (int val : cnts.keySet()) {
            if (cnts.containsKey(k - val)) {
                ans += Math.min(cnts.get(val), cnts.get(k - val));
            }
        }
        return ans / 2;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        long result = maxOperations(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
