import java.util.*;

public class Solution {
    public boolean isThree(int n) {
        // 0ms
        if (n < 3)
            return false;
        double qd = Math.sqrt(n);
        if (qd - (int)qd > 0)
            return false;
        for (int i = 2; i < (int)(qd/2); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        boolean result = isThree(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
