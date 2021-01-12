import java.util.*;

public class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        // 4ms
        if (matrix.length == 0)
            return new int[0];
        int m = matrix.length;
        int n = matrix[0].length;
        int[] res = new int[m*n];
        boolean direction = true;
        int pos = 0;
        for (int i = 0; i < m + n - 1; i++) {
            int up = Math.min(i, m - 1);
            int down = Math.max(i - n + 1, 0);
            if (direction) {
                for (int j = up; j > down - 1; j--) {
                    res[pos++] = matrix[j][i - j];
                }
            } else {
                for (int j = down; j < up + 1; j++) {
                    res[pos++] = matrix[j][i - j];
                }
            }
            direction = !direction;
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_matrix = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(str_matrix);
        System.out.println("matrix = " + ml.matrixToString(matrix));

        long start = System.currentTimeMillis();

        int[] result = findDiagonalOrder(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
