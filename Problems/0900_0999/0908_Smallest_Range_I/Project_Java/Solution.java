import java.util.*;

public class Solution {
    public int smallestRangeI(int[] A, int K) {
        int mx = A[0], mn = A[0];
        for (int a : A) {
            mx = Math.max(mx, a);
            mn = Math.min(mn, a);
        }
        return Math.max(0, mx - mn - 2 * K);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        String[] data;
        
        int[] A = ml.str_to_int_array(flds[0]);
        int K = Integer.parseInt(flds[1]);

        System.out.println("A = " + ml.output_int_array(A));
        System.out.println("K = " + Integer.toString(K));

        long start = System.currentTimeMillis();

        int result = smallestRangeI(A, K);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
