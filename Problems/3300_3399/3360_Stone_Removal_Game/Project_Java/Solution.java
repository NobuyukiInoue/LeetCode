import java.util.*;

public class Solution {
    public boolean canAliceWin(int n) {
        // 0ms
        int pile = 10, count = 0;
        while (n >= pile) {
            n -= pile;
            pile--;
            count++;
        }
        return count%2 != 0;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        boolean result = canAliceWin(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
