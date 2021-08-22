import java.util.*;

public class Solution {
    public int[] findPeakGrid(int[][] mat) {
        // 0ms
        return check2dPeak(0, mat[0].length, mat);
    }

    public int[] check2dPeak(int low, int high, int[][] arr) {
        int mid = low + (high - low) / 2;
        int col_max = 0;
        int row = 0, col = mid;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i][mid] > col_max) {
                col_max = arr[i][mid];
                row = i;
                col = mid;
            }
        }
        if (col > 0 && arr[row][col] < arr[row][col - 1])
            return check2dPeak(low, col, arr);
        else if (col + 1 < arr[row].length && arr[row][col] < arr[row][col + 1])
            return check2dPeak(col, high, arr);
        else
            return new int[] {row, col};
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] mat = ml.stringToIntIntArray(str_mat);
        System.out.println("mat = " + ml.matrixToString(mat));

        long start = System.currentTimeMillis();

        int[] result = findPeakGrid(mat);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
