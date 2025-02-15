import java.util.*;

public class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        // 1ms - 2ms
        int cnt = 1, pre_max_cnt = 0, res = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums.get(i) > nums.get(i - 1)) {
                cnt++;
            } else {
                pre_max_cnt = cnt;
                cnt = 1;
            }
            res = Math.max(res, Math.max(cnt/2, Math.min(pre_max_cnt, cnt)));
        }
        return res >= k;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        List<Integer> nums = ml.stringToListIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.listIntArrayToString(nums) + ", k = " + k);

        long start = System.currentTimeMillis();

        boolean result = hasIncreasingSubarrays(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
