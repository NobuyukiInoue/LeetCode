import java.util.*;

public class Solution {

    public int numSub(String s) {
        // 5ms
        int res = 0, count = 0, mod = (int)1e9 + 7;
        for (int i = 0; i < s.length(); i++) {
            count = s.charAt(i) == '1' ? count + 1: 0;
            res = (res + count) % mod;
        }
        return res;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = numSub(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
