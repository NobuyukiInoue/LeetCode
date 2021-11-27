import java.util.*;

public class Solution {
    public int maxDistance(int[] colors) {
        // 0ms
        int res = 0;
        for (int i = 0; i < colors.length; i++) {
            if (colors[i] != colors[0]) {
                res = Math.max(res, i);
            }
            if (colors[i] != colors[colors.length - 1]) {
                res = Math.max(res, colors.length - 1 - i);
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] colors = ml.stringToIntArray(flds);
        System.out.println("colors = " + ml.intArrayToString(colors));

        long start = System.currentTimeMillis();

        int result = maxDistance(colors);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
