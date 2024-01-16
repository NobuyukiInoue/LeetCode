import java.util.*;

public class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        // 1ms
        int max_diag = 0, max_area = 0;
        for (int[] rect : dimensions) {
            int area = rect[0]*rect[1];
            int diag = rect[0]*rect[0] + rect[1]*rect[1];
            if (diag > max_diag || diag == max_diag && area > max_area) {
                max_diag = diag;
                max_area = area;
            }
        }
        return max_area;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] dimensions = ml.stringToIntIntArray(str_mat);
        System.out.println("dimensions = " + ml.intIntArrayToString(dimensions));

        long start = System.currentTimeMillis();

        int result = areaOfMaxDiagonal(dimensions);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
