import java.util.*;

public class Solution {
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        // 2ms
        HashSet<Integer> hs = new HashSet<>(Arrays.asList(dis(p1, p2), dis(p1, p3), dis(p1, p4), dis(p2, p3), dis(p2, p4), dis(p3, p4)));
        return !hs.contains(0) && hs.size() == 2;
    }

    int dis(int[] a, int[] b){
        return (a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1]);
    }

    double line1, line2;
    public boolean validSquare2(int[] p1, int[] p2, int[] p3, int[] p4) {       
        // 1ms
        line1 = 0.0;
        line2 = 0.0;
        return (decider(p1, p2) && decider(p1, p3) && decider(p1, p4) && decider(p2, p3) && decider(p2, p4) && decider(p3, p4));
    }
    
    public boolean decider(int[] x1, int[] x2) {  
        double dist = Math.sqrt(Math.pow((x2[0] - x1[0]), 2) + Math.pow((x2[1] - x1[1]), 2));
        if (dist == 0.0) {
            return false;
        } else if (line1 == 0.0) {
            line1 = dist;
        } else if (line2 == 0.0 && dist != line1) {
            line2 = dist;
        } else if (dist != line1 && dist != line2) {
            return false;
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] points = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[] p1 = ml.stringToIntArray(points[0]);
        int[] p2 = ml.stringToIntArray(points[1]);
        int[] p3 = ml.stringToIntArray(points[2]);
        int[] p4 = ml.stringToIntArray(points[3]);
        System.out.println("p1 = " + ml.intArrayToString(p1));
        System.out.println("p2 = " + ml.intArrayToString(p2));
        System.out.println("p3 = " + ml.intArrayToString(p3));
        System.out.println("p4 = " + ml.intArrayToString(p4));

        long start = System.currentTimeMillis();

        boolean result = validSquare(p1, p2, p3, p4);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
