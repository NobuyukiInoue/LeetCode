import java.util.*;

public class Solution {
    public int numberOfMatches(int n) {
        // 0ms
        int res = 0;
        int matches;

        while (n > 1) {
            if (n % 2 == 1) {
                matches = n / 2;
                n = matches + 1;
            } else {
                matches = n / 2;
                n = matches;
            }
            res += matches;
        }

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = numberOfMatches(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
