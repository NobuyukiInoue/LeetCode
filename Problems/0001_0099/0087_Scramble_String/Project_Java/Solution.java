import java.util.*;

public class Solution {
    public boolean isScramble(String s1, String s2) {
        // 2ms
        if (s1.equals(s2))
            return true;

        int[] letters = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            letters[s1.charAt(i) - 'a']++;
            letters[s2.charAt(i) - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (letters[i] != 0) {
                return false;
            }
        }
    
        for (int i = 1; i < s1.length(); i++) {
            if (isScramble(s1.substring(0, i), s2.substring(0, i))
             && isScramble(s1.substring(i), s2.substring(i))) {
                return true;
            }
            if (isScramble(s1.substring(0, i), s2.substring(s2.length()-i))
             && isScramble(s1.substring(i), s2.substring(0,s2.length()-i))) {
                return true;
            }
        }
        return false;
    }

    public boolean isScramble_bad(String s1, String s2) {
        return isScramble_bad(s1, 0, s1.length(), s2, 0, s2.length());
    }

    public boolean isScramble_bad(String s1, int s1_start, int s1_end, String s2, int s2_start, int s2_end) {
        int m = s1_end;
        int n = s2_end;

        if (s1_start + 1 > s1_end || s2_start + 1 > s2_end)
            return false;

        char[] s1array = new char[s1_end - s1_start];
        int pos = 0;
        for (int i = s1_start; i < s1_end; i++) {
            s1array[pos++] = s1.charAt(i);
        }

        char[] s2array = new char[s2_end - s2_start];
        pos = 0;
        for (int i = s2_start; i < s2_end; i++) {
            s2array[pos++] = s2.charAt(i);
        }

        Arrays.sort(s1array);
        Arrays.sort(s2array);

        if (m != n || new String(s1array).equals(new String(s2array)) == false)
            return false;
        if (n < 4 || s1.substring(s1_start, s1_end).equals(s2.substring(s2_start, s2_end)))
            return true;

        for (int i = 1; i < n; i++) {
            if (isScramble_bad(s1, s1_start, i, s2, s2_start, i) && isScramble_bad(s1, i, m, s2, i, n)
             || isScramble_bad(s1, s1_start, i, s2, n - i, n) && isScramble_bad(s1, i, m, s2, n - i, n)) {
                return true;
            }
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String s1 = flds[0];
        String s2 = flds[1];
        System.out.println("s1 = " + s1 + ", s2 = " + s2);

        long start = System.currentTimeMillis();

        boolean result = isScramble(s1, s2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
