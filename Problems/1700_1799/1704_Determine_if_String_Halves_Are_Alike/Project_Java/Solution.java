import java.util.*;

public class Solution {
    public boolean halvesAreAlike(String s) {
        // 3ms
        char[] vowls = new char[] {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int mid = s.length()/ 2;
        int cnt = 0;
        for (int i = 0; i < mid; i++) {
            for (char ch : vowls) {
                if (s.charAt(i) == ch) {
                    cnt++;
                }
            }
        }
        for (int i = mid; i < s.length(); i++) {
            for (char ch : vowls) {
                if (s.charAt(i) == ch) {
                    cnt--;
                }
            }
        }
        return cnt == 0;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        boolean result = halvesAreAlike(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
