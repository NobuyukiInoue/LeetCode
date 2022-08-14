import java.util.*;

public class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        // 1ms
        HashMap<Integer, Integer> occ = new HashMap<>();
        for (int num : nums) {
            occ.put(num, 1);
        }
        int ans = 0;
        for (int num : nums) {
            if (occ.containsKey(num + diff) && occ.containsKey(2*(num + diff) - num)) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int diff = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", diff = " + Integer.toString(diff));

        long start = System.currentTimeMillis();

        int result = arithmeticTriplets(nums, diff);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
