import java.util.*;

public class Solution {
    public String greatestLetter(String s) {
        // 1ms
        char capital = 'Z';
        char small = 'z';
        while (capital >= 'A') {
            if (s.indexOf(small) != -1 && s.indexOf(capital) != -1) {
                return "" + capital;
            }
            capital--;
            small--;
        }
        return "";
    }

    public String greatestLetter_arr(String s) {
        // 5ms - 6ms
        int[] upper = new int[26];
        int[] lower = new int[26];
        for (char ch :s.toCharArray()) {
            if (ch <= 'Z') {
                upper[ch - 'A']++;
            } else {
                lower[ch - 'a']++;
            }
        }
        for (int i = upper.length - 1; i >= 0; i--) {
            if (upper[i] > 0 && lower[i] > 0) {
                return Character.toString('A' + i);
            }
        }
        return "";
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = greatestLetter(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
