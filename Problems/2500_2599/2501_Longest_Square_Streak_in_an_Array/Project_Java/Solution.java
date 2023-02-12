import java.util.*;

public class Solution {
    public int longestSquareStreak(int[] nums) {
        // 43ms - 47ms
        Set<Long> set = new HashSet<>();
        for (int num : nums) {
            set.add(Long.valueOf(num));
        }
        int max = 0;
        for (int num : nums) {
            int cnt = 1;
            long l_num = num;
            while (set.contains(l_num*l_num)) {
                l_num = l_num*l_num;
                cnt++;
            }
            max = Math.max(max, cnt);
        }
        return max == 1 ? -1: max;
    }

    public int longestSquareStreak2(int[] nums) {
        // 68ms - 69ms
        Arrays.sort(nums);
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = nums.length - 1; i >= 0; i--)
            map.put(nums[i], map.getOrDefault(nums[i]*nums[i], 0) +1);
        int max = 0;
        for(int val : map.values())
            max = Math.max(max, val);
        return max == 1 ? -1 : max;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = longestSquareStreak(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
