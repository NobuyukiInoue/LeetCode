import java.util.*;

public class Solution {
    public boolean hasMatch(String s, String p) {
        // 1ms
        int index = p.indexOf('*');
        int firstpos = s.indexOf(p.substring(0, index)); 
        int secondpos = s.indexOf(p.substring(index + 1), firstpos + index); 
        if (firstpos != -1 && secondpos != -1) {
            return true;
        }
        return false;
    }

    public void Main(String temp) {
        String flds[] = temp.replace("[", "").replace("]", "").replace(", ", ",").replace("\"", "").trim().split(",");

        String s = flds[0];
        String p = flds[1];
        System.out.println("s = \"" + s + "\", p = \"" + p + "\"");

        long start = System.currentTimeMillis();

        boolean result = hasMatch(s, p);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
