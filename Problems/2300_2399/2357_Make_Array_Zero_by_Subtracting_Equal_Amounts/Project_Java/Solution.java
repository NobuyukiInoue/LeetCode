import java.util.*;

public class Solution {
    public int minimumOperations(int[] nums) {
        // 1ms
        HashSet<Integer> elements = new HashSet<>();
        for (int n : nums) {
            if (n > 0) {
                elements.add(n);
            }
        }
        return elements.size();
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minimumOperations(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
