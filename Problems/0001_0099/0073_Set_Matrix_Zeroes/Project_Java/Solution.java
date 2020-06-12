import java.util.*;

public class Solution {
    public void setZeroes(int[][] matrix) {
        // 1ms
        int m = matrix.length, n = matrix[0].length, k = 0;

        while (k < n && matrix[0][k] != 0)
            ++k;

        for (int i = 1; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (matrix[i][j] == 0)
                    matrix[0][j] = matrix[i][0] = 0;

        for (int i = 1; i < m; ++i)
            for (int j = n - 1; j >= 0; --j)
                if (matrix[0][j] == 0 || matrix[i][0] == 0)
                    matrix[i][j] = 0;

        if (k < n)
            Arrays.fill(matrix[0], 0);        
    }

    private String intintArrayToString(Mylib ml, int[][] data) {
        if (data.length <= 0) {
            return "";
        }

        StringBuilder sb = new StringBuilder("[\n  " + ml.intArrayToString(data[0]));
        for (int i = 1; i < data.length; i++) {
            sb.append("\n, " + ml.intArrayToString(data[i]));
        }

        sb.append("\n]");
        return sb.toString();
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        String[] str_matrix = flds.split("\\],\\[");
        Mylib ml = new Mylib();
        int[][] matrix = new int[str_matrix.length][];
            for (int i = 0; i < str_matrix.length; i++) {
            matrix[i] = ml.stringTointArray(str_matrix[i]);
        }

        System.out.println("matrix = \n" + intintArrayToString(ml, matrix));

        long start = System.currentTimeMillis();
        
        setZeroes(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = \n" + intintArrayToString(ml, matrix));
        System.out.println((end - start)  + "ms\n");
    }
}
