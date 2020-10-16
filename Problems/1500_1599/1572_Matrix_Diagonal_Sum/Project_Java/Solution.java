import java.util.*;

public class Solution {
    public int diagonalSum(int[][] mat) {
        // 0ms
        int total = 0;
        for (int i = 0; i < mat.length; i++) {
            total += mat[i][i] + mat[mat.length - 1 - i][i];
        }

        return mat.length % 2 == 0 ? total : total - mat[mat.length/2][mat.length/2];
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        String[] str_mat = flds.split("\\],\\[");
        Mylib ml = new Mylib();
        int[][] mat = new int[str_mat.length][];
            for (int i = 0; i < str_mat.length; i++) {
            mat[i] = ml.stringTointArray(str_mat[i]);
        }

        System.out.println("mat = [");
        for (int i = 0; i < mat.length; i++) {
            if (i == 0)
                System.out.println("  " + ml.intArrayToString(mat[i]));
            else
                System.out.println(", " + ml.intArrayToString(mat[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();

        int result = diagonalSum(mat);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
