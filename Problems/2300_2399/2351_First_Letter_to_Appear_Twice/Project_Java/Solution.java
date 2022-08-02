import java.util.*;

public class Solution {
    public char repeatedCharacter(String s) {
        // 0ms
        int[] dic = new int[26];
        for (char ch : s.toCharArray()) {
            if (dic[ch - 'a'] == 1) {
                return ch;
            }
            dic[ch - 'a']++;
        }
        return '0';
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        char result = repeatedCharacter(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
