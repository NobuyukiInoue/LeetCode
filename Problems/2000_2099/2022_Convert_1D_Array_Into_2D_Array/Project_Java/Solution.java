import java.util.*;

public class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        // 3ms
        if (m*n != original.length) {
            return new int[][]{};
        }
        int[][] ans = new int[m][n];
        int pos = 0;
        for(int i = 0; i < m; i++){
             for(int j =0; j < n; j++){
                 ans[i][j] = original[pos++];
             }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] original = ml.stringToIntArray(flds[0]);
        int m = Integer.parseInt(flds[1]);
        int n = Integer.parseInt(flds[2]);
        System.out.println("original = " + ml.intArrayToString(original) + ", m = " + Integer.toString(m) + ", n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int[][] result = construct2DArray(original, m, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
