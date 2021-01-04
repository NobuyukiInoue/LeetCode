import java.util.*;

public class Solution {
    public boolean isIdealPermutation(int[] A) {
        // 1ms
        for (int i = 0; i < A.length; i++) {
            if (Math.abs(A[i] - i) > 1) {
                return false;
            }
        }
        return true;
    }

    public boolean isIdealPermutation_normal(int[] A) {
        // 1ms
        int cmax = 0;
        for (int i = 0; i < A.length - 2; ++i) {
            cmax = Math.max(cmax, A[i]);
            if (cmax > A[i + 2]) return false;
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds);
        System.out.println("A = " + ml.intArrayToString(A));

        long start = System.currentTimeMillis();

        boolean result = isIdealPermutation(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
