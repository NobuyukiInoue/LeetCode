import java.util.*;

public class Solution {
    private int[] bit;
    
    public List<Integer> countSmaller(int[] nums) {
        List<Integer> res = new ArrayList<>();
        if (nums.length == 0)
            return res;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for (int n : nums) {
            max = Math.max(n, max);
            min = Math.min(n, min);
        }
        bit = new int[max - min + 2];
        for (int i = nums.length - 1; i >= 0; i--) {
            res.add(sum(nums[i] - min));
            add(nums[i] - min + 1);
        }
        Collections.reverse(res);
        return res;
    }
    
    private int lowbit(int i) {
        return i & -i;
    }
    
    private int sum(int k) {
        int sum = 0;
        for (; k > 0; k -= lowbit(k)) {
            sum += bit[k];
        }
        return sum;
    }
    
    private void add(int k) {
        for (; k < bit.length; k += lowbit(k)) {
            bit[k]++;
        }
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        List<Integer> result = countSmaller(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
