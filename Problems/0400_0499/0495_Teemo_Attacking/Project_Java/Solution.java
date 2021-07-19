import java.util.*;

public class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        // 1ms
        int total = duration;
        for (int i = timeSeries.length - 2; i >= 0; i--) {
            int diff = timeSeries[i + 1] - timeSeries[i];
            if (diff > duration) {
                total += duration;
            } else { 
                total += diff;
            }
        }
        return total;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] timeSeries = ml.stringToIntArray(flds[0]);
        int duration = Integer.parseInt(flds[1]);
        System.out.println("timeSeries = " + ml.intArrayToString(timeSeries));
        System.out.println("duration = " + Integer.toString(duration));

        long startT = System.currentTimeMillis();

        int result = findPoisonedDuration(timeSeries, duration);

        long endT = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((endT - startT)  + "ms\n");
    }
}
