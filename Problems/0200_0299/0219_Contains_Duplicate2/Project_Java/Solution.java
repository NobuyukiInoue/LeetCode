import java.util.*;

public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (i > k)
                set.remove(nums[i-k-1]);
            if (!set.add(nums[i]))
                return true;
        }
        return false;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.str_to_int_array(flds[0]);
        int k = Integer.parseInt(flds[1]);

        System.out.println("nums[] = " + ml.output_int_array(nums));
        System.out.println("k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        boolean result = containsNearbyDuplicate(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " +  Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
