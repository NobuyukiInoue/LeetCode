import java.util.*;

public class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int even = 0, odd = 1;
        while (true) {
            while (even < A.length && A[even] % 2 == 0)
                even += 2;
            while (odd < A.length && A[odd] % 2 != 0)
                odd += 2;
            if (odd >= A.length || even >= A.length)
                return A;
			
            int temp = A[even];
            A[even] = A[odd];
            A[odd] = temp;
        }
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();

        int[] A = ml.str_to_int_array(flds);
        System.out.println("A = " + ml.output_int_array(A));

        long start = System.currentTimeMillis();

        int[] result = sortArrayByParityII(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}
