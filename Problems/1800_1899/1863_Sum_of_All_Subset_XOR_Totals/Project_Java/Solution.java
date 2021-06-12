import java.util.*;

public class Solution {
    public int subsetXORSum(int[] nums) {
        // 1ms
        return sums(nums, 0, 0);
    }

    private int sums(int[] nums, int term, int idx) {
        if (idx == nums.length)
            return term;
        return sums(nums, term, idx + 1) + sums(nums, term ^ nums[idx], idx + 1);
    }

    public int subsetXORSum2(int[] nums) {
        // 19ms
        int result = 0;
        ArrayList<Integer> subsets = new ArrayList<>();
        subsets.add(0);
        for (int n : nums) {
            ArrayList<Integer> new_subsets = new ArrayList<Integer>(subsets);
            for (int s : subsets) {
                new_subsets.add(s ^ n);
                result += new_subsets.get(new_subsets.size() - 1);
            }
            subsets = new_subsets;
        }
        return result;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = subsetXORSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
