import java.util.*;

public class Solution {
    public String freqAlphabets(String s) {
        // 0ms
        StringBuilder sb=new StringBuilder();
        char[] str = s.toCharArray();
        for (int i = 0; i < str.length; i++) {
            if (i < str.length - 2 && str[i + 2] == '#') {
                int n = (str[i] - '0')*10 + (str[i + 1] - '0');
                sb.append((char)('j' + n - 10));
                i += 2;
            }
            else
                sb.append((char)('a' + str[i] - '1'));
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = freqAlphabets(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
