import java.util.*;

public class Solution {
    public int minDeletionSize(String[] A) {
        if (A.length == 0) {
            return 0;
        }

        int result = 0;
        for (int i = 0; i < A[0].length(); i++) {
            for (int j = 0; j < A.length - 1; j++) {
                if (A[j].charAt(i) > A[j + 1].charAt(i)) {
                    result++;
                    break;
                }
            }
        }
        return result;
    }

    public void Main(String temp) {
        String[] A = temp.replace("\"", "").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("A = " + ml.stringArrayToString(A));

        long start = System.currentTimeMillis();

        int result = minDeletionSize(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
