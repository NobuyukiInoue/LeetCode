import java.util.*;

public class Solution {
    public String decodeString(String s) {
        // 0ms
        StringBuilder sb = new StringBuilder();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c <= '9' && c >= '0') {
                count = count * 10 + c -'0';
            } else if (c == '[') {
                int j = i + 1;
                int open = 1, close = 0;
                i++;
                while (i < s.length() && open != close) {
                    if (s.charAt(i) == '[')
                        open++;
                    else if (s.charAt(i) == ']')
                        close++;
                    i++;
                }
                String sub = decodeString(s.substring(j,--i));
                for (int f = 0; f < count; f++) {
                    sb.append(sub);
                }
                count = 0;
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String s = temp.replace(" ", "").replace("[\"", "").replace("\"]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        String result = decodeString(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
