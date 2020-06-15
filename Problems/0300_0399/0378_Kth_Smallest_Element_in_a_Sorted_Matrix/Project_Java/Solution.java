import java.util.*;

public class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        // 0ms
        int n = matrix.length;
        int lo = matrix[0][0], hi = matrix[n - 1][n - 1];
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int count = getLessEqual(matrix, mid);
            if (count < k) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
    
    private int getLessEqual(int[][] matrix, int val) {
        int res = 0;
        int n = matrix.length, i = n - 1, j = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] > val) {
                i--;
            } else {
                res += i + 1;
                j++;
            }
        }
        return res;
    }

    public int kthSmallest2(int[][] matrix, int k) {
        // 6ms
        int m = matrix.length;
        int n = matrix[0].length;
        int[] data = new int[m*n];
        int pos = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                data[pos++] = matrix[i][j];
            }
        }
        
        Arrays.sort(data);

        return data[k - 1];
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
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").trim().split("\\]],\\[");
        String[] str_matrix = flds[0].split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] matrix;
        if (flds[0].length() > 0) {
            matrix = new int[str_matrix.length][];
            for (int i = 0; i < str_matrix.length; i++) {
                matrix[i] = ml.stringTointArray(str_matrix[i]);
            }
            System.out.println("matrix = \n" + intintArrayToString(ml, matrix));
        } else {
            matrix = null;
            System.out.println("matrix = []\n");
        }

        int k = Integer.parseInt(flds[1].replace("]]",""));
        System.out.println("k = " + Integer.toString(k));

        long start = System.currentTimeMillis();
        
        int result = kthSmallest(matrix, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
