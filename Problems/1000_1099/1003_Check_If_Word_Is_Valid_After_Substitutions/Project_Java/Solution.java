import java.util.*;

public class Solution {
    public boolean isValid(String s) {
        // 6ms
        while (s.indexOf("abc") >= 0) {
            s = s.replace("abc", "");
        }
        return s == "";
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        boolean result = isValid(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
