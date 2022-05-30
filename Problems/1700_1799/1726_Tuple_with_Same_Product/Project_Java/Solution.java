import java.util.*;

public class Solution {
    public int tupleSameProduct(int[] nums) {
        // 305ms - 336ms
        int ans = 0;
        HashMap<Integer, Integer> cnts = new HashMap<>();
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int prod = nums[i] * nums[j];
                int freq = cnts.getOrDefault(prod, 0);
                ans = ans + freq * 8;
                cnts.put(prod, freq + 1);
            }
        }
        return ans;
    }

    public int tupleSameProduct_normal(int[] nums) {
        // 337ms - 548ms
        HashMap<Integer, Integer> cnts = new HashMap<>();
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                cnts.put(nums[i]*nums[j], cnts.getOrDefault(nums[i]*nums[j], 0) + 1);
            }
        }
        int ans = 0;
        for (int cnt : cnts.values()) {
            if (cnt > 1) {
                ans += (cnt*(cnt - 1)/2)*8;
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

        int result = tupleSameProduct(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
