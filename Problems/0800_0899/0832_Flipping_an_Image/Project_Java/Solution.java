import java.util.*;

public class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int n = A.length;
        for (int[] row : A)
            for (int i = 0; i * 2 < n; i++)
                if (row[i] == row[n - i - 1])
                    row[i] = row[n - i - 1] ^= 1;
        return A;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] A = ml.stringToIntIntArray(flds);
        System.out.println("A = " + ml.matrixToString(A));

        long start = System.currentTimeMillis();

        int[][] result = flipAndInvertImage(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.matrixToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
