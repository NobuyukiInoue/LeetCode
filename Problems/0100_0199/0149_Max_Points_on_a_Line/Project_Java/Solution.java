import java.util.*;

public class Solution {
    public int maxPoints(int[][] points) {
        // 22ms - 23ms
        if (points.length <= 2) {
            return points.length;
        }
        int res = 0;
        for (int i = 0; i < points.length; i++) {
            int cur = 0, overlap = 0;
            HashMap<Double, Integer> lines = new HashMap<>();
            for (int j = i + 1; j < points.length; j++) {
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                if (dx == 0 && dy == 0) {
                    overlap++;
                    continue;
                }
                double key;
                if (dx == 0) {
                    key = Double.MAX_VALUE;
                } else {
                    key = 10.0*(double)dy/dx;
                }
                if (key == 0.0) key = 0.0;
                lines.put(key, lines.getOrDefault(key, 0) + 1);
                cur = Math.max(cur, lines.get(key));
            }
            res = Math.max(res, cur + overlap);
        }
        return res + 1;
    }

    public int maxPoints1(int[][] points) {
        // 18ms
        int maxP = 0, coordinates = points.length;
        if (coordinates < 3) {
            return coordinates;
        }
        for (int i = coordinates - 1; i > 0; i--) {
            int i_x = points[i][0];
            int i_y = points[i][1];
            Map<Double, Integer> hashmap = new HashMap<>(); 
            for (int j = i + 1; j <coordinates; j++) {
                double dy = points[j][1] - i_y;
                double dx = points[j][0] - i_x;
                if (dx != 0) {
                    hashmap.merge(dy/dx, 1, Integer::sum);
                } else {
                    hashmap.merge(Double.MAX_VALUE, 1, Integer::sum);
                }
            }
            for (int k = i - 1; k >= 0; k--) {
                double dy = i_y - points[k][1];
                double dx = i_x - points[k][0];
                if (dx != 0) {
                    hashmap.merge(dy/dx, 1, Integer::sum);
                } else {
                    hashmap.merge(Double.MAX_VALUE, 1, Integer::sum);
                }
            }
            maxP = ((Collections.max(hashmap.values()) + 1) > maxP) ?
                    Collections.max(hashmap.values()) + 1 : maxP;
        }
        return maxP;
    }

    public int maxPoints2(int[][] points) {
        // 45ms - 48ms
        int res = 2;
        int n = points.length;
        if (n == 1) {
            return 1;
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int extra = 2;
                for (int k = 0; k < n; k++) {
                    if (k == i || k == j) {
                        continue;
                    }
                    int p1 = points[i][0]*(points[j][1] - points[k][1]);
                    int p2 = points[j][0]*(points[k][1] - points[i][1]);
                    int p3 = points[k][0]*(points[i][1] - points[j][1]);
                    if (p1 + p2 + p3 == 0) {
                        extra++;
                    }
                }
                res = Math.max(res, extra);
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] points = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("points = " + ml.intIntArrayToString(points));

        long start = System.currentTimeMillis();

        int result = maxPoints(points);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
