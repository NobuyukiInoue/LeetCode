import java.util.*;

public class Solution {
    public int[] sumZero(int n) {
        // 0ms
        int[] A = new int[n];
        int n2 = n / 2 + 1;
        for (int i = 1, j = 0; i < n2; i++, j += 2) {
            A[j] = -i;
            A[j + 1] = i;
        }
        return A;
    }

    public int[] sumZero2(int n) {
        // 0ms
        int[] A = new int[n];
        for (int i = 0; i < n; ++i)
            A[i] = i * 2 - n + 1;
        return A;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));
        Mylib ml = new Mylib();

        long start = System.currentTimeMillis();

        int[] result = sumZero(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
