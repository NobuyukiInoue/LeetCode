import java.util.*;

public class Solution {
    public boolean canThreePartsEqualSum(int[] A) {
        int sum = 0;
        for (int i = 0; i < A.length; i++)
            sum += A[i];

        if (sum % 3 != 0)
            return false;

        int sum_part = 0, count = 0, hit = sum / 3;
        for (int i = 0; i < A.length; i++) {
            sum_part += A[i];
            if (sum_part == hit) {
                sum_part = 0;
                count++;
            }
        }

        if (count == 3)
            return true;
        else
            return false;
    }
    
    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();

        int[] A = ml.str_to_int_array(flds);

        System.out.println("A = " + ml.output_int_array(A));

        long start = System.currentTimeMillis();
        
        boolean result = canThreePartsEqualSum(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
