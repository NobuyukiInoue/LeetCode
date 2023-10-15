import java.util.*;

public class Solution {
    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
        // 1ms
        int ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (Integer.bitCount(i) == k) {
                ans += nums.get(i);
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        List<Integer> nums = ml.stringToListIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.listIntArrayToString(nums) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        int result = sumIndicesWithKSetBits(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
