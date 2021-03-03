import java.util.*;

public class Solution {
    public int findMaxLength(int[] nums) {
        // 18ms
        HashMap<Integer, Integer> dic = new HashMap<>();
        dic.put(0, -1);
        int total = 0, ans = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                total--;
            } else {
                total++;
            }
            if (dic.containsKey(total)) {
                ans = Math.max(i - dic.get(total), ans);
            } else {
                dic.put(total, i);
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

        int result = findMaxLength(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
