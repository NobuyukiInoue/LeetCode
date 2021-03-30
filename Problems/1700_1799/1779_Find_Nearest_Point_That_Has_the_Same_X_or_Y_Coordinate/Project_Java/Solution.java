import java.util.*;

public class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        // 1ms
        int smallest = Integer.MAX_VALUE, index = -1;
        for (int i = 0; i < points.length; i++) {
            if (points[i][0] == x || points[i][1] == y) {
                if (points[i][0] == x && points[i][1] == y) {
                    return i;
                }
                int calced = Math.abs(points[i][0] - x + points[i][1] - y);
                if (calced < smallest) {
                    smallest = calced;
                    index = i;
                }
            }
        }
        return index;
    }

    public int nearestValidPoint2(int x, int y, int[][] points) {
        // 4ms
        int smallest = Integer.MAX_VALUE, index = -1;
        int dx, dy, mh;
        for (int i = 0; i <  points.length; i++) {
            dx = x - points[i][0];
            dy = y - points[i][1];
            mh = Math.abs(dx) + Math.abs(dy);
            if (dx * dy == 0 && mh < smallest) {
                smallest = mh;
                index = i;
            }
        }
        return index;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("]]]", "").trim().split("\\],\\[\\[");

        String[] flds0 = flds[0].replace("[[", "").split("\\],\\[");
        int x = Integer.parseInt(flds0[0]);
        int y = Integer.parseInt(flds0[1]);
        System.out.println("x = " + x + ", y = " + y);

        Mylib ml = new Mylib();
        int[][] points = ml.stringToIntIntArray(flds[1].split("\\],\\["));
        System.out.println("points = " + ml.intIntArrayToString(points));

        long start = System.currentTimeMillis();

        int result = nearestValidPoint(x, y, points);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
