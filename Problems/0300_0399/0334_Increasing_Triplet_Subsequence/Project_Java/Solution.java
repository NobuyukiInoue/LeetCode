import java.util.*;

public class Solution {
    public boolean increasingTriplet(int[] nums) {
        // 0ms
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;
        for (int n :  nums) {
            if (n <= first)
                first = n;
            else if (n <= second)
                second = n;
            else
                return true;
        }
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = increasingTriplet(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
