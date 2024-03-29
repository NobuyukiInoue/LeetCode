import java.util.*;

public class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        // 3ms
        int[] mod = new int[k];
        mod[0] = 1;
        int running_mod = 0;
        for (int num : nums) {
            running_mod = (num + running_mod)%k;
            while (running_mod < 0) {
                running_mod += k;
            }
            mod[running_mod]++;
        }
        int ans = 0;
        for (int m : mod) {
            ans += m*(m - 1)/2;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = subarraysDivByK(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
