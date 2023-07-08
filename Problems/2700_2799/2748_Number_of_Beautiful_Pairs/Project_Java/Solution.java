import java.util.*;

public class Solution {
    public int countBeautifulPairs(int[] nums) {
        // 36ms
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int m = nums[i]%10;
            for (int j = 0; j < i; j++) {
                int n = nums[j];
                while (n >= 10) {
                    n /= 10;
                }
                if (gcd(m, n) == 1) {
                    ans++;
                }
            }
        }
        return ans;
    }

    private int gcd(int m, int n) {
        int r;
        while (n > 0) {
            r = m % n;
            m = n;
            n = r;
        }
        return m;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = countBeautifulPairs(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
