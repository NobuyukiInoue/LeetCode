import java.util.*;

public class Solution {
    public int countTestedDevices(int[] batteryPercentages) {
        // 0ms
        int ans = 0;
        for (int target : batteryPercentages) {
            if (target > ans) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] batteryPercentages = ml.stringToIntArray(flds);
        System.out.println("batteryPercentages = " + ml.intArrayToString(batteryPercentages));

        long start = System.currentTimeMillis();

        int result = countTestedDevices(batteryPercentages);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
