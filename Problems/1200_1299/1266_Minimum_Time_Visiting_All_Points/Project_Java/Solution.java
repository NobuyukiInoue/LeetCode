import java.util.*;

public class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        // 1ms
        int total = 0;
        for (int i = 1; i < points.length; i++) {
            total += Math.max(Math.abs(points[i][0] -points[i - 1][0]), Math.abs(points[i][1] -points[i - 1][1]));
        }

        return total;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] points = ml.stringToIntIntArray(flds);
        System.out.println("points = " + ml.intIntArrayToString(points));

        long start = System.currentTimeMillis();

        int result = minTimeToVisitAllPoints(points);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
