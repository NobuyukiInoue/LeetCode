import java.util.*;

public class Solution {
    public int integerReplacement(int n) {
        // 0ms
        int ans = 0;
        while (n != 1) {
            if ((n & 1) == 0)
                n >>>= 1;
            else if (n == 3 || ((n + 1) & n) > ((n - 1) & (n - 2)))
                n--;
            else
                n++;
            ans++;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();
        
        int result = integerReplacement(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
