import java.util.*;

public class Solution {
    public boolean checkValid2(int[][] matrix) {
        // 55ms
        for (int r = 0, n = matrix.length; r < n; ++r) {
            Set<Integer> row = new HashSet<>();
            Set<Integer> col = new HashSet<>();
            for (int c = 0; c < n; c++) {
                if (!row.add(matrix[r][c]) || !col.add(matrix[c][r])) {
                    return false;
                }
            }
        }
        return true;
    }

    public boolean checkValid(int[][] matrix) {
        // 20ms
        for (int r = 0, n = matrix.length; r < n; ++r) {
            BitSet row = new BitSet(n + 1), col = new BitSet(n + 1);
            for (int c = 0; c < n; ++c) {
                if (row.get(matrix[r][c]) || col.get(matrix[c][r])) {
                    return false;
                }
                row.set(matrix[r][c]);
                col.set(matrix[c][r]);
            }
        } 
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(str_mat);
        System.out.println("matrix = " + ml.matrixToString(matrix));

        long start = System.currentTimeMillis();

        boolean result = checkValid(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
