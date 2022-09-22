import java.util.*;

public class Solution {
    public int mostFrequentEven(int[] nums) {
        // 22ms - 54ms
        HashMap<Integer, Integer> cnts = new HashMap<>();
        int ans = Integer.MAX_VALUE,max_cnts = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                cnts.put(num, cnts.getOrDefault(num, 0) + 1);
                if (cnts.get(num) == max_cnts) {
                    ans = Math.min(ans, num);
                }
                if (cnts.get(num) > max_cnts) {
                    max_cnts = cnts.get(num);
                    ans = num;
                }
            }
        }
        if (cnts.size() == 0) {
            return -1;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = mostFrequentEven(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
