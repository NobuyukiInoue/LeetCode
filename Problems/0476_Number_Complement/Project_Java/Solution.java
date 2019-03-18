import java.util.*;

public class Solution {
    public int findComplement(int num) {
        int ones = 0;
        int t = num;
        while (t > 0) {
            ones <<= 1;
            ones |= 1;
            t >>= 1;
        }
        return ones ^ num;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int num = Integer.parseInt(flds);

        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = findComplement(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
