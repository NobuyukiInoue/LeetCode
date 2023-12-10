import java.util.*;

public class Solution {
    public boolean areSimilar(int[][] mat, int k) {
        // 1ms
        int n = mat[0].length;
        for (int[] row : mat) {
            for (int i = 0; i < n; i++) {
                if (row[i] != row[(i + k)%n]) {
                    return false;
                }
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        int[][] mat = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        int k = Integer.parseInt(flds[1].replace("]]", ""));
        System.out.println("mat = " + ml.intIntArrayToString(mat) + ", k = " + k);

        long start = System.currentTimeMillis();

        boolean result = areSimilar(mat, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
