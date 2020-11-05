import java.util.*;

public class Solution {
    public int maxNumberOfBalloons(String text) {
        // 1ms
        int[] map = new int[26];
        char[] chars = text.toCharArray();
        for(int i = 0; i < chars.length; i++) {
            map[chars[i] - 'a']++;
        }
        int ans = text.length();
        for(int i = 0; i < map.length; i++) {
            char c = (char)(i + 'a');
            if (c == 'a' || c == 'b' || c == 'n') {
                ans = Math.min(ans, map[i]);
            } else if (c == 'l' || c == 'o') {
                ans = Math.min(ans, map[i] / 2);
            }
        }
        return ans;
    }

    public int maxNumberOfBalloons2(String text) {
        // 2ms
        int[] count = new int[26];
        int[] countBalloon = new int[26];

        int min = text.length();
        for (int i = 0; i < min; ++i)
            ++count[text.charAt(i) - 'a'];
        for (char c : "balloon".toCharArray())
            ++countBalloon[c - 'a'];
        for (char c : "balloon".toCharArray())
            min = Math.min(min, count[c - 'a'] / countBalloon[c - 'a']);
        
        return min;
    }

    public void Main(String temp) {
        String text = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("text = " + text);

        long start = System.currentTimeMillis();

        int result = maxNumberOfBalloons(text);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
