import java.util.*;

public class Solution {
    public boolean divideArray(int[] nums) {
        // 8ms
        int pairSize = nums.length / 2;
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        int countPairs = 0;
        for (int values: counts.values()) {
            if (values % 2 == 1) {
                return false;
            }
            countPairs += values / 2;
        }
        return countPairs == pairSize;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = divideArray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
