import java.util.*;

public class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] rec1 = ml.stringToIntArray(flds[0]);
        int[] rec2 = ml.stringToIntArray(flds[1]);
        System.out.println("rec1 = " + ml.intArrayToString(rec1));
        System.out.println("rec2 = " + ml.intArrayToString(rec2));

        long start = System.currentTimeMillis();

        boolean result = isRectangleOverlap(rec1, rec2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
