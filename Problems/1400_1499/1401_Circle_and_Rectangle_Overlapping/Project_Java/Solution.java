import java.util.*;

public class Solution {
    public boolean checkOverlap(int radius, int x_center, int y_center, int x1, int y1, int x2, int y2) {
        // 0ms
        double c1 = (x2 + x1) / 2.0;
        double c2 = (y2 + y1) / 2.0;
        double v1 = Math.abs((double)x_center - c1);
        double v2 = Math.abs((double)y_center - c2);
        double h1 = (x2 - x1) / 2.0;
        double h2 = (y2 - y1) / 2.0;
        double u1 = Math.max(0.0, v1 - h1);
        double u2 = Math.max(0.0, v2 - h2);
        return (u1 * u1 + u2 * u2 <= radius * radius);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String[] pt1 = flds[0].split(",");
        int radius = Integer.parseInt(pt1[0]);
        int x_center = Integer.parseInt(pt1[1]);
        int y_center = Integer.parseInt(pt1[2]);

        String[] pt2 = flds[1].split(",");
        int x1 = Integer.parseInt(pt2[0]);
        int y1 = Integer.parseInt(pt2[1]);
        int x2 = Integer.parseInt(pt2[2]);
        int y2 = Integer.parseInt(pt2[3]);

        StringBuilder sb = new StringBuilder();
        Formatter formatter = new Formatter(sb, Locale.JAPANESE);
        System.out.println(formatter.format("radius = %d, x_center = %d, y_center = %d", radius, x_center, y_center));
        System.out.println(formatter.format("x1, y1, x2, y2 = %d, %d, %d, %d", x1, y1, x2, y2));

        long start = System.currentTimeMillis();

        boolean result = checkOverlap(radius, x_center, y_center, x1, y1, x2, y2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
