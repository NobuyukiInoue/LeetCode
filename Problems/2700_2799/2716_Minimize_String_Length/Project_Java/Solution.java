import java.util.*;

public class Solution {
    public int minimizedStringLength(String s) {
        // 9ms
        HashMap<Character, Boolean> cnts = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            cnts.put(s.charAt(i), true);
        }
        return cnts.size();
    }

    public int minimizedStringLength2(String s) {
        // 9ms
        HashMap<Character, Integer> cnts = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            cnts.put(s.charAt(i), 1);
        }
        return cnts.size();
    }

    public int minimizedStringLength3(String s) {
        // 10ms
        HashMap<Character, Integer> cnts = new HashMap<>();
        for (char ch : s.toCharArray()) {
            cnts.put(ch, 1);
        }
        return cnts.size();
    }

    public int minimizedStringLength_1liner(String s) {
        // 19ms
        return (int)s.chars().distinct().count();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        int result = minimizedStringLength(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
