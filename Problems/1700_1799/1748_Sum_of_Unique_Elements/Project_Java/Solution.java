import java.util.*;

public class Solution {
    public int sumOfUnique(int[] nums) {
        // 1ms
        Map<Integer, Integer> dic = new HashMap<>();
        for (int num : nums) {
            dic.put(num, dic.getOrDefault(num, 0) + 1);
        }

        int res = 0;
        for (int num: dic.keySet()){
            if (dic.get(num) == 1) {
                res += num;
            }
        }

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = sumOfUnique(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
