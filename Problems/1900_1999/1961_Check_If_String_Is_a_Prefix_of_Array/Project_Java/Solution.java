import java.util.*;

public class Solution {
    public boolean isPrefixString(String s, String[] words) {
        // 1ms
        int count = 0;
        char[] chars = s.toCharArray();
        for (String word : words) {
            for (char ch : word.toCharArray()) {
                if (count == chars.length) {
                    return false;
                }
                if (chars[count++] != ch) {
                    return false;
                }
            }
            if (count == chars.length) {
                return true;
            }
        }
        return count == chars.length;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        String[] words = flds[1].split(",");
        Mylib ml = new Mylib();

        System.out.println("s = " + s + ", words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        boolean result = isPrefixString(s, words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
