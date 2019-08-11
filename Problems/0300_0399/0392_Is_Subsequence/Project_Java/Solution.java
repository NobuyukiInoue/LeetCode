import java.util.*;

public class Solution {
    public boolean isSubsequence(String s, String t) {
        int presentIndex = -1;
        for(int i = 0; i < s.length(); i++){
            int index = t.indexOf(s.charAt(i), presentIndex + 1);
            if (index > presentIndex) {
                presentIndex = index;
            } else {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        String s = flds[0];
        String t = flds[1];

        System.out.println("s = " + s + ", t = " + t);

        long start = System.currentTimeMillis();
        
        boolean result = isSubsequence(s, t);

        long end = System.currentTimeMillis();

        System.out.println("result = \n" + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
