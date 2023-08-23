import java.util.*;

public class Solution {
    public int maxSum(int[] nums) {
        // 5ms
        HashMap<Integer, Integer> dic = new HashMap<>();
        int res = -1;
        for (int num : nums) {
            int max_digit = get_max_digit(num);
            if (dic.containsKey(max_digit)) {
                res = Math.max(res, num + dic.get(max_digit));
            }
            dic.put(max_digit, Math.max(num, dic.getOrDefault(max_digit, -1)));
        }
        return res;
    }

    private int get_max_digit(int num) {
        int max_digit = 0;
        while (num > 0) {
            max_digit = Math.max(max_digit, num % 10);
            num /= 10;
        }
        return max_digit;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maxSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
