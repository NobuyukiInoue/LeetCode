import java.util.*;

public class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        // 2ms
        int n = A.length;
        int[] cnts = new int[n + 1];
        int[] C = new int[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            if (++cnts[A[i]] == 2) {
                total++;
            }
            if (++cnts[B[i]] == 2) {
                total++;
            }
            C[i] = total;
        }
        return C;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds[0]);
        int[] B = ml.stringToIntArray(flds[1]);
        System.out.println("A = " + ml.intArrayToString(A) + ", B = " + ml.intArrayToString(B));

        long start = System.currentTimeMillis();

        int[] result = findThePrefixCommonArray(A, B);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
