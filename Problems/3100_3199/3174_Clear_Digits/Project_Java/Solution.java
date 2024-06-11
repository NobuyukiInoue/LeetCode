import java.util.*;

public class Solution {
    public String clearDigits(String s) {
        // 2ms
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if ('0' <= ch && ch <= '9') {
                sb.deleteCharAt(sb.length() - 1);
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

        String result = clearDigits(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
