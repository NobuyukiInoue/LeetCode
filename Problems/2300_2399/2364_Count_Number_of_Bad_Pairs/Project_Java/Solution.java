import java.util.*;

public class Solution {
    public long countBadPairs(int[] nums) {
        // 37ms
        long cnt = 0;
        HashMap<Integer,Integer> count_dict = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int prev = count_dict.getOrDefault(i - nums[i], 0);
            cnt += i - prev;
            count_dict.put(i - nums[i], prev + 1);
        }
        return cnt;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        long result = countBadPairs(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
