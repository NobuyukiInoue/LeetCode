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

        int[][] A = new int[flds.length][];
    
        for (int i = 0; i < flds.length; i++) {
            A[i] = ml.stringTointArray(flds[i]);
        }

        System.out.println("A = ");
        for (int i = 0; i < A.length; i++)
            System.out.println(ml.intArrayToString(A[i]));

        long start = System.currentTimeMillis();
        
        int[][] result = tranpose(A);

        long end = System.currentTimeMillis();

        System.out.println("result = ");
        for (int i = 0; i < result.length; i++)
            System.out.println(ml.intArrayToString(result[i]));

        System.out.println((end - start)  + "ms\n");
    }
}
