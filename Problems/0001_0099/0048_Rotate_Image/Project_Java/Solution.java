import java.util.*;

public class Solution {
    public void rotate(int[][] matrix) {
        // 0ms
        int n = matrix.length;
        for (int l = 0; l < n / 2; l++) {
            int r = n - 1 - l;
            for (int p = l; p < r; p++) {
                int q = n - 1 - p;
                int cache = matrix[l][p];
                matrix[l][p] = matrix[q][l];
                matrix[q][l] = matrix[r][q];
                matrix[r][q] = matrix[p][r];
                matrix[p][r] = cache;
            }
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(flds);
        System.out.println("matrix = " + ml.matrixToString(matrix));

        long start = System.currentTimeMillis();

        rotate(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.matrixToString(matrix));
        System.out.println((end - start)  + "ms\n");
    }
}
