import java.util.*;

public class Solution {
    public int numSubmat(int[][] mat) {
        // 4ms
        for (int i = 0; i < mat.length; i++) {
            for (int j = 1; j < mat[0].length; j++) {
                if (mat[i][j] == 1) {
                    if (j > 0) {
                        mat[i][j] = mat[i][j - 1] + 1;
                    }
                }
            }
        }

        int submatrices = 0;
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                if (mat[i][j] > 0) {
                    int min_value = mat[i][j];
                    for (int row = i; row < mat.length && mat[row][j] > 0; row++) {
                        min_value = Math.min(min_value, mat[row][j]);
                        submatrices += min_value;
                    }
                }
            }
        }

        return submatrices;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
    	int[][] mat = ml.stringToIntIntArray(str_mat);
        System.out.println("mat = " + ml.matrixToString(mat));

        long start = System.currentTimeMillis();

        int result = numSubmat(mat);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
