import java.util.*;

public class Solution {
    public int divisorSubstrings(int num, int k) {
        // 0ms
        String str_num = Integer.toString(num);
        int ans = 0;
        for (int i = 0; i < str_num.length() - k + 1; i++) {
            int temp = Integer.parseInt(str_num.substring(i, i + k));
            if (temp != 0 && num % temp == 0) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        int num = nums[0], k = nums[1];
        System.out.println("num = " + Integer.toString(num) + ", k = " + Integer.toString(k));

        long t_start = System.currentTimeMillis();

        int result = divisorSubstrings(num, k);

        long t_end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((t_end - t_start)  + "ms\n");
    }
}
