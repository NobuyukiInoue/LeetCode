import java.util.*;

public class Solution {
    public int removePalindromeSub(String s) {
        // 0ms
        if (s.isEmpty())
            return 0;
        else if (s.equals(new StringBuilder(s).reverse().toString()))
            return 1;
        else
            return 2;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = removePalindromeSub(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
