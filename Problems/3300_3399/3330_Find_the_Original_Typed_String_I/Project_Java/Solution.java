import java.util.*;

public class Solution {
    public int possibleStringCount(String word) {
        // 1ms
        int ans = 0;
        char prev = word.charAt(0);
        for (char ch : word.toCharArray()) {
            if (ch == prev) {
                ans++;
            }
            prev = ch;
        }
        return ans;
    }

    public void Main(String temp) {
        String word = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("word = \"" + word + "\"");

        long start = System.currentTimeMillis();

        int result = possibleStringCount(word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
