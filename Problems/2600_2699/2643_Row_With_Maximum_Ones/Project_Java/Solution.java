import java.util.*;

public class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        // 5ms
        int idx = 0, max_count = 0;
        for (int i = 0; i < mat.length; i++) {
            int cnt = 0;
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] == 1) {
                    cnt++;
                }
            }
            if (cnt > max_count) {
                idx = i;
                max_count = cnt;
            }
        }
        return new int[] {idx, max_count};
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] mat = ml.stringToIntIntArray(str_mat);
        System.out.println("mat = " + ml.matrixToString(mat));

        long start = System.currentTimeMillis();

        int[] result = rowAndMaximumOnes(mat);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
