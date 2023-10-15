import java.util.*;

public class Solution {
    public int xorBeauty1(int[] nums) {
        // 1ms
        int ans = 0;
        for (int num : nums) {
            ans ^= num;
        }
        return ans;
    }

    public int xorBeauty(int[] nums) {
        // 4ms
        return Arrays.stream(nums).reduce((a, b) -> a ^ b).orElse(0);
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = xorBeauty(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
