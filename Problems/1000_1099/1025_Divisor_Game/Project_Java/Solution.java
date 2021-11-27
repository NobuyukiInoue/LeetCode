import java.util.*;

public class Solution {
    public boolean divisorGame(int n) {
        // 0ms
        return n%2 == 0;
    }

    public void Main(String temp) {
        String fld = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        boolean result = divisorGame(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
