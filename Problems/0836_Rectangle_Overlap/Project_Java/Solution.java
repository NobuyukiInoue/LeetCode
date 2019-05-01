import java.util.*;

public class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        
        String[] pt1 = flds[0].split(",");
        int[] rec1 = new int[pt1.length];
        for (int i = 0; i < pt1.length; i++)
            rec1[i] = Integer.parseInt(pt1[i]);

        String[] pt2 = flds[1].split(",");
        int[] rec2 = new int[pt2.length];
        for (int i = 0; i < pt2.length; i++)
            rec2[i] = Integer.parseInt(pt2[i]);
    
        Mylib ml = new Mylib();

        System.out.println("rec1 = " + ml.output_int_array(rec1));
        System.out.println("rec2 = " + ml.output_int_array(rec2));

        long start = System.currentTimeMillis();
        
        boolean result = isRectangleOverlap(rec1, rec2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
