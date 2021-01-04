import java.util.*;

public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        // 0ms
        int[] li = new int[A.length];

        for (int i = 2; i < A.length; i++) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
                li[i] = li[i - 1] + 1;
            }
        }

        int res = 0;
        for (int num : li) {
            res += num;
        }

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds);
        System.out.println("A = " + ml.intArrayToString(A));

        long start = System.currentTimeMillis();

        int result = numberOfArithmeticSlices(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
