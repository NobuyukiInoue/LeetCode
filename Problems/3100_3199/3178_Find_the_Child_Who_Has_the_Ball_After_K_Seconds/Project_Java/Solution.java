import java.util.*;

public class Solution {
    public int numberOfChild(int n, int k) {
        // 1ms
        n--;
        int rounds = k / n, rem = k%n;
        if (rounds%2 == 0)
            return rem;
        return n - rem;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("n = " + n + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = numberOfChild(n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
