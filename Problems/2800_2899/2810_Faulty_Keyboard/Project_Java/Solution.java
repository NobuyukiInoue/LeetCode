import java.util.*;

public class Solution {
    public String finalString(String s) {
        // 3ms
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (ch == 'i') {
                sb.reverse();
            } else {
                sb.append(ch);
            }
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        String result = finalString(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
