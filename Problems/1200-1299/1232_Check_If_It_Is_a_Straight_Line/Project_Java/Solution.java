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

        int[][] coordinates = new int[flds.length][];
    
        for (int i = 0; i < flds.length; i++) {
            coordinates[i] = ml.stringTointArray(flds[i]);
        }

        System.out.print("coordinates = [");
        for (int i = 0; i < coordinates.length; i++) {
            if (i == 0)
                System.out.print(ml.intArrayToString(coordinates[i]));
            else
                System.out.print("," + ml.intArrayToString(coordinates[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        boolean result = checkStraightLine(coordinates);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
