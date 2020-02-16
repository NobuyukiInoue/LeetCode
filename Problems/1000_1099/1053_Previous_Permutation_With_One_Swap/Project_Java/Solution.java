import java.util.*;

public class Solution {
    public int[] prevPermOpt1(int[] A) {
        // 0ms
        int index = -1;
        int min = Integer.MAX_VALUE;
        int n = A.length;
        int number = 0;

        for (int i = n - 1; i > 0; i--) {
            if (A[i] < min)
                min = A[i];
            if (min < A[i - 1]) {
                number = A[i - 1];
                index= i;
                break;
            }            
        }

        if (index == -1)
            return A;
          
        int maxTemp = -1;
        int indexer = -1;
        for (int i = index; i < n; i++) {
            if (A[i] > maxTemp && A[i] < number) {
                maxTemp  = A[i];
                indexer = i;
            }
        }
     
        int temper = A[indexer];
        A[indexer] = A[index - 1];
        A[index - 1] = temper;

        return A;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] A = ml.stringTointArray(flds);
        System.out.println("A = " + ml.intArrayToString(A));

        long start = System.currentTimeMillis();
        
        int[] result = prevPermOpt1(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
