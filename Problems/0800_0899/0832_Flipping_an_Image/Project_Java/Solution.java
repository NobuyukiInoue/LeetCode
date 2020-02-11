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

        int[][] A = new int[flds.length][];
    
        for (int i = 0; i < flds.length; i++) {
            A[i] = ml.stringTointArray(flds[i]);
        }

        System.out.println("A = ");
        for (int i = 0; i < A.length; i++)
            System.out.println(ml.intArrayToString(A[i]));

        long start = System.currentTimeMillis();
        
        int[][] result = flipAndInvertImage(A);

        long end = System.currentTimeMillis();

        System.out.println("result = ");
        for (int i = 0; i < result.length; i++)
            System.out.println(ml.intArrayToString(result[i]));

        System.out.println((end - start)  + "ms\n");
    }
}
