import java.util.*;

public class Solution {
    public boolean isMatch(String s, String p) {
        // 5ms
        int m = s.length(), n = p.length();
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (p.charAt(i) == '*')
                count++;
        }

        if (count == 0 && m != n)
            return false;
        else if (n - count > m)
            return false;

        boolean[] match = new boolean[m + 1];
        match[0] = true;

        for (int i = 0; i < m; i++) {
            match[i + 1] = false;
        }

        for (int i = 0; i < n; i++) {
            if (p.charAt(i) == '*') {
                for (int j = 0; j < m; j++) {
                    match[j + 1] = match[j] || match[j + 1];
                }
            } else {
                for (int j = m - 1; j >= 0; j--) {
                    match[j + 1] = (p.charAt(i) == '?' || p.charAt(i) == s.charAt(j)) && match[j];
                }
                match[0] = false;
            }
        }

        return match[m];
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").trim().split(",");
        String s = flds[0];
        String p = flds[1];
        System.out.println("s = " + s + ", p = " + p);

        long start = System.currentTimeMillis();
        
        Boolean result = isMatch(s, p);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
