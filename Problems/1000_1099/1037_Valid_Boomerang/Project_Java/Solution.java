import java.util.*;

public class Solution {
    public boolean isBoomerang(int[][] points) {
        return (points[0][0] - points[1][0]) * (points[0][1] - points[2][1]) != (points[0][0] - points[2][0]) * (points[0][1] - points[1][1]);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int[][] points = new int[flds.length][];
    
        for (int i = 0; i < flds.length; i++) {
            points[i] = ml.stringTointArray(flds[i]);
        }

        System.out.print("points = [");
        for (int i = 0; i < points.length; i++) {
            if (i == 0)
                System.out.print("[" + ml.intArrayToString(points[i]) + "]");
            else
                System.out.print(",[" + ml.intArrayToString(points[i]) + "]");
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        boolean result = isBoomerang(points);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
