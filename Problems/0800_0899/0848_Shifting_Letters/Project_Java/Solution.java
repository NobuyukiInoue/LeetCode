import java.util.*;

public class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        // 2ms
        int acum = 0;
        char[] s2 = s.toCharArray();
        for (int i = s.length() - 1; i >= 0; i--) {
            acum = (acum + shifts[i]) % 26;
            s2[i] = (char)(97 + (s2[i] + acum - 97) % 26);
        }
        return new String(s2);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String s = flds[0];
        int[] shifts = ml.stringToIntArray(flds[1]);
        System.out.println("s = " + s);
        System.out.println("shifts = " + ml.intArrayToString(shifts));

        long start = System.currentTimeMillis();

        String result = shiftingLetters(s, shifts);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
