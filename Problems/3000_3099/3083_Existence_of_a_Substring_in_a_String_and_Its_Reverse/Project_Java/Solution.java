import java.util.*;

public class Solution {
    public boolean isSubstringPresent(String s) {
        // 1ms - 2ms
        String r_s = new StringBuilder(s).reverse().toString();
        while (r_s.length() > 1) {
            if (s.contains(r_s.substring(0, 2))) {
                return true;
            }
            r_s = r_s.substring(1);
        }
        return false;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        Boolean result = isSubstringPresent(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
