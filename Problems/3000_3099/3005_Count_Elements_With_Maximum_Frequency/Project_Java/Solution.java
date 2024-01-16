import java.util.*;

public class Solution {
    public int maxFrequencyElements(int[] nums) {
        // 2ms
        HashMap<Integer, Integer> cnts = new HashMap<>();
        for (int num : nums) {
            cnts.put(num, cnts.getOrDefault(num, 0) + 1);
        }
        int max_cnts = 0;
        for (Integer val : cnts.values()) {
            max_cnts = Math.max(max_cnts, val);
        }
        int ans = 0;
        for (Integer val : cnts.values()) {
            if (val == max_cnts) {
                ans += val; 
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maxFrequencyElements(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
