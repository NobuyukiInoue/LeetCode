import java.util.*;

public class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        // 0ms
        double dx = coordinates[1][0] - coordinates[0][0];
        if (dx == 0)
            return false;
        double inclination = (coordinates[1][1] - coordinates[0][1]) / dx;
        for (int i = 1; i < coordinates.length - 1; i++) {
            dx = coordinates[i + 1][0] - coordinates[i][0];
            if (dx == 0)
                return false;
            if ((coordinates[i + 1][1] - coordinates[i][1]) / dx != inclination)
                return false;
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] coordinates = ml.stringToIntIntArray(flds);
        System.out.println("coordinates = " + ml.intIntArrayToString(coordinates));

        long start = System.currentTimeMillis();

        boolean result = checkStraightLine(coordinates);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
