import java.util.*;

public class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n > 0 && (n & (n - 1)) == 0)
            return true;
        else
            return false;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);

        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        Boolean result = isPowerOfTwo(n);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
