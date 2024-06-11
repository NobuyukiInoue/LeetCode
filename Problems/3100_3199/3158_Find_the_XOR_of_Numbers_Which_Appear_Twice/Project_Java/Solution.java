import java.util.*;

public class Solution {
    public int duplicateNumbersXOR(int[] nums) {
        // 3ms - 4ms
        HashMap<Integer, Integer> cnts = new HashMap<>();
        for (int num : nums) {
            cnts.put(num, cnts.getOrDefault(num, 0) + 1);
        }
        int ans = 0;
        for (int k : cnts.keySet()) {
            if (cnts.get(k) == 2) {
                ans ^= k;
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

        int result = duplicateNumbersXOR(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
