import java.util.*;

public class Solution {
    public boolean isPalindrome(int x) {
        // 7ms
        String temp = Integer.toString(x);

        for (int i = 0; i < temp.length() / 2; i++) {
            if (temp.charAt(i) != temp.charAt(temp.length() - 1 - i))
                return false;
        }

        return true;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        int x = Integer.parseInt(fld);
        System.out.println("x = " + Integer.toString(x));

        long start = System.currentTimeMillis();

        boolean result = isPalindrome(x);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
