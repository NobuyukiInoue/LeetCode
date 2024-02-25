import java.util.*;

public class Solution {
    public boolean isPossibleToSplit(int[] nums) {
        // 1ms
        int[] cnts = new int[100];
        for (int num : nums) {
            if (++cnts[num - 1] == 3) {
                return false;
            }
        }
        return true;
    }

    public boolean isPossibleToSplit2(int[] nums) {
        // 2ms
        HashMap<Integer, Integer> cnts = new HashMap<>();
        for (int num : nums) {
            cnts.put(num, cnts.getOrDefault(num, 0) + 1);
            if (cnts.get(num) == 3) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = isPossibleToSplit(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
