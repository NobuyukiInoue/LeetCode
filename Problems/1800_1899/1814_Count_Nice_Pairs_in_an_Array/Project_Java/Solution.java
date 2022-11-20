import java.util.*;

public class Solution {
    public int countNicePairs(int[] nums) {
        // 67ms - 87ms
        Map<Integer,Integer> dic = new HashMap<>();
        int count = 0;
        for (int num : nums){
            int temp = num - reverse(num);
            count += dic.getOrDefault(temp, 0);
            count %= 1000000007;
            dic.put(temp, dic.getOrDefault(temp, 0) + 1);
        }
        return count;
    }

    public int reverse(int num){
        int ans = 0;
        while (num != 0 ) {
            ans = ans*10 + num%10;
            num /= 10;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = countNicePairs(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
