import java.util.*;

public class Solution {
    public int smallestNumber(int n) {
        // 0ms
        int cur = 1;
        while (cur - 1 < n) {
            cur <<= 1;
        }
        return cur - 1;
    }

    public int smallestNumber2(int n) {
        // 0ms
        return (1 << (Integer.SIZE - Integer.numberOfLeadingZeros(n))) - 1;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        int result = smallestNumber(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
