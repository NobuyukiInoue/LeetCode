import java.util.*;

public class Solution {
    public int matrixScore(int[][] A) {
        // 0ms
        int r = A.length, c = A[0].length;
        int answer = r * (1 << (c - 1));
        for (int j = 1; j < c; j++) {
            int count = 0;
            for (int i = 0; i < r; i++) {
                count += (A[i][0] == 1) ? A[i][j] : A[i][j] ^ 1;
            }
            answer += Math.max(r - count, count) * (1 << (c - 1 - j));
        }
        return answer;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] matrixStr = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] A = ml.stringToIntIntArray(matrixStr);
        System.out.println("A = " + ml.matrixToString(A));

        long start = System.currentTimeMillis();

        int result = matrixScore(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
