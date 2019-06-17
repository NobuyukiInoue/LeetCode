import java.util.*;

public class Solution {
    public int lastRemaining(int n) {
        if (n == 1)
            return 1;
        if (n <= 3)
            return 2;
        if ((n/2) % 2 == 1)
            return 4*lastRemaining((n - 2)/4);
        else
            return 4*lastRemaining(n/4) - 2;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        int result = lastRemaining(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
