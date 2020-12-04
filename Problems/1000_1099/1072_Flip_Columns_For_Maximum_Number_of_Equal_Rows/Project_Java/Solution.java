import java.util.*;

public class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        // 41ms
        Map<String, Integer> map = new HashMap<>();

        for (int[] row : matrix) {
            StringBuilder sb1 = new StringBuilder();
            StringBuilder sb2 = new StringBuilder();
            for (int col : row) {
                sb1.append(col);
                sb2.append(1 - col);
            }
            String str1 = sb1.toString();
            String str2 = sb2.toString();
            map.put(str1, map.getOrDefault(str1,0) + 1);
            map.put(str2, map.getOrDefault(str2,0) + 1);
        }

        int res = 0;
        for (int v : map.values())
            res = Math.max(res, v);

        return res;
    }
 
    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] matrix = new int[flds.length][];
        for (int i = 0; i < matrix.length; i++)
            matrix[i] = ml.stringToIntArray(flds[i]);
        System.out.println("matrix = " + ml.intIntArrayToString(matrix));

        long start = System.currentTimeMillis();

        int result = maxEqualRowsAfterFlips(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
