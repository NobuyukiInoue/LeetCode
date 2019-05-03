import java.util.*;

public class Solution {
    public int peakIndexInMountainArray(int[] A) {
        for (int i = 1; i + 1 < A.length; ++i)
            if (A[i] > A[i + 1])
                return i;
        return 0;
    }
    
    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();

        int[] A = ml.str_to_int_array(flds);

        System.out.println("A = " + ml.output_int_array(A));

        long start = System.currentTimeMillis();
        
        int result = peakIndexInMountainArray(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
