import java.util.*;

public class Solution {
    public int smallestNumber(int n, int t) {
        // 0ms
        for ( ; getProd(n)%t != 0; n++);
        return n;
    }

    private int getProd(int n) {
        int prod = 1;
        while (n > 0) {
            prod *= n%10;
            n /= 10;
        }
        return prod;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int t = Integer.parseInt(flds[1]);
        System.out.println("n = " + n + ", t = " + t);

        long start = System.currentTimeMillis();

        int result = smallestNumber(n, t);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
