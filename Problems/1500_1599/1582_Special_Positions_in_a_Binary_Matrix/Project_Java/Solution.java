import java.util.*;

public class Solution {
    public int numSpecial(int[][] mat) {
        // 0ms
        int result = 0;
        for (int[] row : mat) {
            if (arraySum(row) == 1) {
                if (getColumnSum(mat, getIndex(row)) == 1)
                    result += 1;
            }
        }
        return result;
    }

    private int getIndex(int[] row) {
        for (int j = 0; j < row.length; j++) {
            if (row[j] == 1) {
                return j;
            }
        }
        return -1;
    }

    private int getColumnSum(int[][]mat, int i) {
        int total = 0;
        for (int[] row : mat) {
            total += row[i];
        }
        return total;
    }

    private int arraySum(int[] row) {
        int total = 0;
        for (int col : row) {
            total += col;
        }
        return total;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] mat = ml.stringToIntIntArray(str_mat);
        System.out.println("mat = " + ml.matrixToString(mat));

        long start = System.currentTimeMillis();

        int result = numSpecial(mat);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
