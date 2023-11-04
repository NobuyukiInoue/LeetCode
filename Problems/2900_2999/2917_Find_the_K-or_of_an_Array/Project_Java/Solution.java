import java.util.*;

public class Solution {
    public int findKOr(int[] nums, int k) {
        // 3ms
        int ans = 0;
        for (int i = 0; i < 31; i++) {
            int rep = (1 << i);
            int cnt = 0;
            for (int num : nums) {
                if ((rep & num) != 0) {
                    cnt++;
                }
            }
            if (cnt >= k) {
                ans += rep;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        int result = findKOr(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
