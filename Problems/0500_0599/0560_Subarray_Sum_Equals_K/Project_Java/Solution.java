import java.util.*;

public class Solution {
    public int subarraySum(int[] nums, int k) {
        // 17ms
        HashMap<Integer, Integer> preSums = new HashMap<Integer, Integer>();
        preSums.put(0, 1);
        int s = 0, res = 0;
        for (int num : nums) {
            s += num;
            res += preSums.getOrDefault(s - k, 0);
            preSums.put(s, preSums.getOrDefault(s, 0) + 1);
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = subarraySum(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
