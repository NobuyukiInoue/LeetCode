import java.util.*;

public class Solution {
    public int sumOfEncryptedInt(int[] nums) {
        // 1ms
        int ans = 0;
        for (int num : nums) {
            int l = 0, m = 0;
            for (; num > 0; l++) {
                m = Math.max(m, num%10);
                num /= 10;
            }
            for ( ;l > 0; l--) {
                ans += m;
                m *= 10;
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

        int result = sumOfEncryptedInt(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
