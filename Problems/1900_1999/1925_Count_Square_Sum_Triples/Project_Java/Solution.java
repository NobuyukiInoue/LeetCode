import java.util.*;

public class Solution {
    public int countTriples(int n) {
        // 5ms
        int ans = 0;
        int[] nums = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            nums[i] = i;
        }
        for (int i = n; i >= 1; i--) {
            int l = 0, r = i - 1;
            while (l < r) {
                if (nums[l]*nums[l] + nums[r]*nums[r] == nums[i]*nums[i]) { 
                    ans += 2;
                    l++;
                    r--;
                }                                                
                else if (nums[l]*nums[l] + nums[r]*nums[r] < nums[i]*nums[i]) {
                    l++;
                }
                else {
                    r--;
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = countTriples(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
