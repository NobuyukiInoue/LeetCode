import java.util.*;

public class Solution {
    public int kthGrammar(int n, int k) {
        // 0ms
        return Integer.bitCount(k - 1) & 1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("n = " + Integer.toString(n) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = kthGrammar(n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
