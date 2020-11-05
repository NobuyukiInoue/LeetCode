import java.util.*;

public class Solution {
    public int singleNumber(int[] nums) {
        // 0ms
        int ones = 0;
        int twos = 0;
        for (int value : nums) {
            ones = (ones ^ value) & ~twos;
            twos = (twos ^ value) & ~ones;
        }
        return ones;
    }

    public int singleNumber2(int[] nums) {
        // 4ms
        List<Integer> res = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        for (int target : nums) {
            int val;
            if (map.containsKey(target)) {
                val = map.get(target) + 1;
            } else {
                val = 1;
            }
            map.put(target, val);
        }

        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            if (entry.getValue() == 1) {
                return entry.getKey();
            }
        }

        return 0;
    }

    public int singleNumber3(int[] nums) {
        //  4ms
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            int sum = 0;
            for (int j = 0; j < nums.length; j++) {
                if (((nums[j] >> i) & 1) == 1) {
                    sum++;
                    sum %= 3;
                }
            }
            if (sum != 0) {
                ans |= sum << i;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = singleNumber(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
