import java.util.*;

public class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        // 0ms
        for (int i = 0; i < 4; ++i) {
            if (Arrays.deepEquals(mat, target)) {
                return true;
            }
            rotate(mat);
        }
        return false;
    }
    private void rotate(int[][] mat) {
        for (int i = 0, j = mat.length - 1; i < j; ++i, --j) {
            int[] tmp = mat[i];
            mat[i] = mat[j];
            mat[j] = tmp;
        } 
        for (int r = 0, R = mat.length; r < R; ++r) {
            for (int c = r + 1; c < R; ++c) {
                int tmp = mat[r][c];
                mat[r][c] = mat[c][r];
                mat[c][r] = tmp;
            }
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").replace("]]]", "").trim().split("\\]\\],\\[\\[");

        Mylib ml = new Mylib();
        int[][] mat = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        int[][] target = ml.stringToIntIntArray(flds[1].split("\\],\\["));
        System.out.println("mat = " + ml.matrixToString(mat));
        System.out.println("target = " + ml.matrixToString(target));

        long start = System.currentTimeMillis();

        boolean result = findRotation(mat, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
