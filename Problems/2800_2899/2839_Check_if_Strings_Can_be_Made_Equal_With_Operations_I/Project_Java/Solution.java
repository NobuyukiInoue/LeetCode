import java.util.*;

public class Solution {
    public boolean canBeEqual(String s1, String s2) {
        // 1ms
        if (s1.equals(s2)) {
            return true;
        }
        char[] arr_s1 = s1.toCharArray();
        for (int i = 0; i < 2; i++) {
            if (arr_s1[i] == s2.charAt(i + 2)) {
                char ct = arr_s1[i];
                arr_s1[i] = arr_s1[i + 2];
                arr_s1[i + 2] = ct;
            }
            if (String.valueOf(arr_s1).equals(s2)) {
                return true;
            }
        }
        return false;
    }

    public boolean canBeEqual1(String s1, String s2) {
        // 1ms
        if (s1.charAt(0) !=s2.charAt(0) && s1.charAt(2)!=s2.charAt(2)) {
            if(s1.charAt(0) != s2.charAt(2) || s1.charAt(2) != s2.charAt(0)) {
                return false;
            }
        } else if (s1.charAt(0) != s2.charAt(0) && s1.charAt(2) == s2.charAt(2) || s1.charAt(0) == s2.charAt(0) && s1.charAt(2) != s2.charAt(2)) {
            return false;
        }
        if (s1.charAt(1) != s2.charAt(1) && s1.charAt(3) != s2.charAt(3)) {
            if (s1.charAt(1) != s2.charAt(3) || s1.charAt(3) != s2.charAt(1)) {
                return false;
            }
        } else if (s1.charAt(1) == s2.charAt(1) && s1.charAt(3) != s2.charAt(3) || s1.charAt(1) != s2.charAt(1) && s1.charAt(3) == s2.charAt(3)) {
            return false;
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s1 = flds[0];
        String s2 = flds[1];
        System.out.println("s1 = \"" + s1 + "\", s2 = \"" + s2 + "\"");

        long start = System.currentTimeMillis();

        boolean result = canBeEqual(s1, s2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
