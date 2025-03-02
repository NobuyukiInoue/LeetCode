import java.util.*;

public class Solution {
    public int minOperations(int[] nums, int k) {
        // 2ms - 3ms
        Map<Integer, Boolean> elems = new HashMap<>();
        int min = nums[0];
        for (int num : nums) {
            if (num > k) {
                elems.put(num, true);
                min = Math.min(min, num);
            } else if (num < k) {
                return -1;
            }
        }
        return elems.size() + (min < k ? -1 : 0);
    }

    public int minOperations2(int[] nums, int k) {
        // 5ms
        Set<Integer> elems = new TreeSet<>();
        for (int num : nums) {
            elems.add(num);
        }

        int min = elems.iterator().next();
        if (min < k) {
            return -1;
        }
        return elems.size() + (min == k ? -1 : 0);     
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = minOperations(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
