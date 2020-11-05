import java.util.*;

public class Solution {
    public double trimMean(int[] arr) {
        // 2ms
        int n = arr.length;
        double sum = 0d;
        Arrays.sort(arr);
        for (int i = n/20; i < n - n/20; i++) {
            sum += arr[i];
        }
        return sum/(n*9/10);
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        double result = trimMean(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Double.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
