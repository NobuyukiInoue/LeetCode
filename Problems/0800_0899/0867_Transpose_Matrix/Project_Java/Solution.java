import java.util.*;

public class Solution {
    public int[][] tranpose(int[][] A) {
        int M = A.length, N = A[0].length;
        int[][] B = new int[N][M];
        for (int j = 0; j < N; j++)
            for (int i = 0; i < M; i++)
                B[j][i] = A[i][j];
        return B;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] A = ml.stringToIntIntArray(flds);
        System.out.println("A = " + ml.matrixToString(A));

        long start = System.currentTimeMillis();

        int[][] result = tranpose(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.matrixToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
