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

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_matrix = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(str_matrix);
        System.out.println("matrix = \n" + ml.matrixToString(matrix));

        long start = System.currentTimeMillis();

        setZeroes(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = \n" + ml.matrixToString(matrix));
        System.out.println((end - start)  + "ms\n");
    }
}
