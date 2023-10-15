import java.util.*;

public class Solution {
    public int minOperations(List<Integer> nums, int k) {
        // 1ms - 2ms
        Long left = (1l << k) - 1; 
        for (int n = nums.size(), i = n-1; i >= 0; --i) {
            if (nums.get(i) <= k && (left & 1l << nums.get(i) - 1) > 0) {
                left ^= 1l << nums.get(i) - 1;
            }
            if (left == 0) {
                return n - i;
            }
        }
        return -1;
    }

    public int minOperations2(List<Integer> nums, int k) {
        // 1ms
        int[] check = new int[k + 1];
        int i, cnt = 0;
        for (i = nums.size() - 1; i > 0; i--) {
            int num = nums.get(i);
            if (num <= k) {
                if (check[num] == 0) {
                    check[num] = 1;
                    cnt++;
                    if (cnt == k) {
                        return nums.size() - i;
                    }
                }
            }
        }
        return nums.size() - i;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        List<Integer> nums = ml.stringToListIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.listIntArrayToString(nums) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        int result = minOperations(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
