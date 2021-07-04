import java.util.*;

public class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        // 0ms
        for (int i = left; i <= right; i++) {
            boolean result = false;
            for (int[] work : ranges) {
                if (work[0] <= i && i <= work[1]) {
                    result = true;
                    break;
                }
            }
            if (!result) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        int[][] ranges = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        int[] flds2 = ml.stringToIntArray(flds[1].replace("]]", ""));
        int left = flds2[0];
        int right = flds2[1];
        System.out.println("ranges = " + ml.matrixToString(ranges));
        System.out.println("left = " + Integer.toString(left) + ", right = " + Integer.toString(right));
        long start = System.currentTimeMillis();

        boolean result = isCovered(ranges, left, right);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
