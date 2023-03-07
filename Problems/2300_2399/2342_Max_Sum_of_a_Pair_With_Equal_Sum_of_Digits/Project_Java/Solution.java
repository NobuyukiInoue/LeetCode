import java.util.*;

public class Solution {
    public int maximumSum(int[] nums) {
        // 59ms
        HashMap<Integer, Integer> dict_map = new HashMap<>();
        int max_val = -1;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int digits_sum = 0;
            while (num > 0) {
                digits_sum += num % 10;
                num /= 10;
            }
            if (dict_map.containsKey(digits_sum)) {
                int new_max_val = nums[i] + dict_map.get(digits_sum);
                max_val = Math.max(max_val, new_max_val);
                dict_map.put(digits_sum, Math.max(nums[i], dict_map.get(digits_sum)));
            } else {
                dict_map.put(digits_sum, nums[i]);
            }
        }
        return max_val;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maximumSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
