import java.util.*;

public class Solution {
    public int minDominoRotations(int[] A, int[] B) {
        // 3ms
        int countA = getCount(A[0], A, B);
        int countB = getCount(B[0], A, B);
        if (countA == -1 && countB == -1)
            return -1;
        if (countA == -1)
            return countB;
        if (countB == -1)
            return countA;
        return Math.min(countA,countB);
    }
    
    public int getCount(int x, int[] A, int[] B){
        int nA = 0;
        int nB = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] != x && B[i] != x)
                return -1;
            if (A[i] != x)
                nA++;
            if (B[i] != x)
                nB++;
        }
        return Math.min(nA, nB);
    }

    public int minDominoRotations2(int[] A, int[] B) {
        // 5ms
        int[] countA = new int[7], countB = new int[7], same = new int[7];
        int n = A.length;
        for (int i = 0; i < n; ++i) {
            countA[A[i]]++;
            countB[B[i]]++;
            if (A[i] == B[i])
                same[A[i]]++;
        }
        for (int i  = 1; i < 7; ++i)
            if (countA[i] + countB[i] - same[i] == n)
                return n - Math.max(countA[i], countB[i]);
        return -1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds[0]);
        int[] B = ml.stringToIntArray(flds[1]);
        System.out.println("A = " + ml.intArrayToString(A));
        System.out.println("B = " + ml.intArrayToString(B));

        long start = System.currentTimeMillis();

        int result = minDominoRotations(A, B);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
