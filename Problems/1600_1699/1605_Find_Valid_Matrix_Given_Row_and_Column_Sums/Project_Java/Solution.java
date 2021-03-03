import java.util.*;

public class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        // 1ms
        int[][] matrix = new int[rowSum.length][];
        for (int i = 0; i < rowSum.length; i++) {
            matrix[i] = new int[colSum.length];
        }

        int i = 0, j = 0;
        while (i < rowSum.length && j < colSum.length) {
            matrix[i][j] = Math.min(rowSum[i], colSum[j]);
            if (rowSum[i] == colSum[j]) {
                i++;
                j++;
            } else if (rowSum[i] > colSum[j]) {
                rowSum[i] -= colSum[j];
                j++;
            } else {
                colSum[j] -= rowSum[i];
                i++;
            }
        }
        return matrix;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] rowSum = ml.stringToIntArray(flds[0]);
        int[] colSum = ml.stringToIntArray(flds[1]);
        System.out.println("rowSum = " + ml.intArrayToString(rowSum));
        System.out.println("colSum = " + ml.intArrayToString(colSum));

        long start = System.currentTimeMillis();

        int[][] result = restoreMatrix(rowSum, colSum);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.matrixToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
