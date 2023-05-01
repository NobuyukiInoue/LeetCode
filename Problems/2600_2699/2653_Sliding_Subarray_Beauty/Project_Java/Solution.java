import java.util.*;

public class Solution {
    public int[] getSubarrayBeauty(int[] nums, int k, int x) {
        // 38ms - 41ms
        int[] freq = new int[51];
        int[] ans = new int[nums.length - k + 1];
        int idx = 0;
        for (int i = 0, j = 0; i < nums.length; i++) {
            if (nums[i] < 0) {
                freq[Math.abs(nums[i])]++;
            }
            if (i - j + 1 >= k) {
                int cnt = 0;
                for (int L = 50; L > 0; L--) {
                    cnt += freq[L];
                    if (cnt >= x) {
                        ans[idx++] = -L;
                        break;
                    }
                }
                if (cnt < x)
                    ans[idx++] = 0;
                if (nums[j] < 0)
                    freq[Math.abs(nums[j])]--;
                j++;
            }
        }
        return ans; 
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        int x = Integer.parseInt(flds[2]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k + ", x = " + x);
 
        long start = System.currentTimeMillis();

        int[] result = getSubarrayBeauty(nums, k, x);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
