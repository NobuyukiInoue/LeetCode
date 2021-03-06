import java.util.*;

public class Solution {
    public int largestSumAfterKNegations(int[] A, int K) {
        // 1ms
        Arrays.sort(A);
        for (int i = 0, j = 0; i < K; i++, A[j]=-A[j] )
            if (j + 1 < A.length && A[j+1] < A[j])
                j++;
        int sum = 0;
        for (int i = 0; i < A.length; i++)
            sum += A[i];
        return sum;
    }

    public int largestSumAfterKNegations2(int[] A, int K) {
        // 35ms
        Arrays.sort(A);
        for (int i = 0; i < A.length; i++) {
            if (K == 0)
                return Arrays.stream(A).sum();
            if (A[i] >= 0)
                break;
            A[i] = -A[i];
            K--;
        }

        Arrays.sort(A);
        if (K % 2 == 1)
            A[0] = -A[0];
        return Arrays.stream(A).sum();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds[0]);
        int K = Integer.parseInt(flds[1]);

        System.out.println("A = " + ml.intArrayToString(A));
        System.out.println("K = " + Integer.toString(K));

        long start = System.currentTimeMillis();

        int result = largestSumAfterKNegations(A, K);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
