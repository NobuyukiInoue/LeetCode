import java.util.*;

public class Solution {
    public int[] shortestToChar(String S, char C) {
        int n = S.length();
        int[] res = new int[n];
        int pos = -n;
        for (int i = 0; i < n; ++i) {
            if (S.charAt(i) == C) pos = i;
            res[i] = i - pos;
        }
        for (int i = n - 1; i >= 0; --i) {
            if (S.charAt(i) == C)  pos = i;
            res[i] = Math.min(res[i], Math.abs(i - pos));
        }
        return res;
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String S = words[0];
        char C = words[1].charAt(0);
        System.out.println("S = " + S + ", C = " + C);
        Mylib ml = new Mylib();

        long start = System.currentTimeMillis();
        
        int[] result = shortestToChar(S, C);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}
