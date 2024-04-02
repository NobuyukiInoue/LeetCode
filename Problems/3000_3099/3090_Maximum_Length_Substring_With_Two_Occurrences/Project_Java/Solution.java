import java.util.*;

public class Solution {
    public int maximumLengthSubstring(String s) {
        // 1ms
        int ans = 0, j = 0;
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
            while (freq[s.charAt(i) - 'a'] == 3) {
                freq[s.charAt(j++) - 'a']--;
            }
            ans = Math.max(ans, i - j + 1);
        }
        return ans;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        int result = maximumLengthSubstring(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
