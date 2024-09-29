import java.util.*;

public class Solution {
    public String longestNiceSubstring(String s) {
        // 3ms
        if (s.equals("")) {
            return "";
        }
        HashSet<Character> ss = new HashSet<>();
        for (char ch : s.toCharArray()) {
            ss.add(ch);
        }
        for (int i = 0; i < s.length(); i++) {
            if (!ss.contains(Character.toLowerCase(s.charAt(i))) || !ss.contains(Character.toUpperCase(s.charAt(i)))) {
                String s0 = longestNiceSubstring(s.substring(0, i));
                String s1 = longestNiceSubstring(s.substring(i+1));
                if (s0.length() >= s1.length()) {
                    return s0;
                }
                return s1;
            }
        }
        return s;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        String result = longestNiceSubstring(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
