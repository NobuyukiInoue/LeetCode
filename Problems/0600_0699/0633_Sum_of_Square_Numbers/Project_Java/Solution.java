import java.util.*;

public class Solution {
    public boolean judgeSquareSum(int c) {
        int i = 0;
        int j = (int)Math.sqrt(c);

        while (i <= j) {
            int sum = i*i + j*j;
            if (i*i+j*j == c)
                return true;
            else if (sum < c)
                i++;
            else j--;
        }

        return false;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int c = Integer.parseInt(flds);
        System.out.println("num = " + Integer.toString(c));

        long start = System.currentTimeMillis();

        boolean result = judgeSquareSum(c);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
