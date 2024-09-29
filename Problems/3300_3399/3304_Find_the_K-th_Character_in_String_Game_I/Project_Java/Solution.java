import java.util.*;

public class Solution {
    public char kthCharacter(int k) {
        // 0ms
        return (char)('a' + Integer.bitCount(k - 1));
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int k = Integer.parseInt(flds);
        System.out.println("k = " + k);

        long start = System.currentTimeMillis();

        char result = kthCharacter(k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
