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

    private String intIntArrayToString(Mylib ml, int[][] matrix) {
        String resultStr = "[" + ml.output_int_array(matrix[0]);
        for (int i = 1; i < matrix.length; i++) {
            resultStr +=  "," + ml.output_int_array(matrix[i]);
        }
        resultStr += "]";
        return resultStr;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int[][] matrix = new int[flds.length][];
    
        for (int i = 0; i < matrix.length; i++) {
            matrix[i] = ml.str_to_int_array(flds[i]);
        }

        System.out.println("matrix = " + intIntArrayToString(ml, matrix));

        long start = System.currentTimeMillis();
        
        rotate(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + intIntArrayToString(ml, matrix));
        System.out.println((end - start)  + "ms\n");
    }
}
