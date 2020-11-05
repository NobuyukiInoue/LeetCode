import java.util.*;

public class Solution {
    public int[] getNoZeroIntegers(int n) {
        // 1ms
        for (int a = 1; a < n; a++) {
            int b = n - a;
            if (!String.valueOf(a).contains("0") && !String.valueOf(b).contains("0"))
                return new int[]{a, b};
        }
        return new int[]{}; 
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        int[] result = getNoZeroIntegers(n);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
