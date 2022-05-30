import java.util.*;

public class Solution {
    public int percentageLetter(String s, char letter) {
        // 0ms
        int cnt = 0;
        for (char ch : s.toCharArray()) {
            if (ch == letter) {
                cnt++;
            }
        }
        return 100*cnt/s.length();
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").split(",");
        String s = flds[0];
        char letter = flds[1].charAt(0);
        System.out.println("s = " + s + ", letter = " + letter);

        long start = System.currentTimeMillis();

        int result = percentageLetter(s, letter);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
