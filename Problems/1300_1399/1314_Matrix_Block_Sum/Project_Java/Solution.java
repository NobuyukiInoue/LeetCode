import java.util.*;

public class Solution {
    public int[][] matrixBlockSum(int[][] mat, int K) {
        // 2ms
        int r = mat.length;
        int c = mat[0].length;
        int[][] temp = new int[r][c];
        int[][] answer = new int[r][c];

        for (int i = 0; i < r; i++) {
            int res = 0;
            for (int delta_c = 0; delta_c < K + 1; delta_c++) {
                if (delta_c < c) {
                    res += mat[i][delta_c];
                }
            }
            temp[i][0] = res;
        }

        for (int i = 0; i < r; i++) {
            int res = temp[i][0];
            for (int j = 1; j < c; j++) {
                int remove_c = j - K - 1;
                if (0 <= remove_c && remove_c < c) {
                    res -= mat[i][remove_c];
                }
                int add_c = j + K;
                if (0 <= add_c && add_c < c) {
                    res += mat[i][add_c];
                }
                temp[i][j] = res;
            }
        }

        for (int i = 0; i < c; i++) {
            int res = 0;
            for (int delta_r = 0; delta_r < K + 1; delta_r++) {
                res += temp[delta_r][i];
            }
            answer[0][i] = res;
        }

        for (int i = 0; i < c; i++) {
            int res = answer[0][i];
            for (int j = 1; j < r; j++) {
                int remove_r = j - K - 1;
                if (0 <= remove_r && remove_r < r) {
                    res -= temp[remove_r][i];
                }
                int add_r = j + K;
                if (0 <= add_r && add_r < r) {
                    res += temp[add_r][i];
                }
                answer[j][i] = res;
            }
        }

        return answer;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        String[] str_mat = flds[0].replace("[[[", "").split("\\],\\[");
        int[][] mat = ml.stringToIntIntArray(str_mat);
        int K = Integer.parseInt(flds[1].replace("]]", ""));
        System.out.println("mat = " + ml.intIntArrayToString(mat) + ", K = " + Integer.toString(K));

        long start = System.currentTimeMillis();

        int[][] result = matrixBlockSum(mat, K);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
