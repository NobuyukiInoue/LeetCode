import java.util.*;

public class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        // 1ms
        int n = nums.size();
        int ans[] = new int[n];
        for (int i = 0; i < n; i++) {
            int num = nums.get(i);
            if (nums.get(i) % 2 == 0) {
                ans[i] = -1;
            } else {
                ans[i] = num - ((num + 1)&(-num - 1))/2;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        List<Integer> nums = ml.stringToListIntArray(flds);
        System.out.println("nums = " + ml.listIntArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = minBitwiseArray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
