import java.util.*;

public class Solution {
    public int[] sortArrayByParity(int[] A) {
        for (int i = 0, j = 0; j < A.length; j++)
            if (A[j] % 2 == 0) {
                int tmp = A[i];
                A[i++] = A[j];
                A[j] = tmp;;
            }
        return A;
    }
    
    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();

        int[] A = ml.str_to_int_array(flds);

        System.out.println("A = " + ml.output_int_array(A));

        long start = System.currentTimeMillis();
        
        int[] result = sortArrayByParity(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}
