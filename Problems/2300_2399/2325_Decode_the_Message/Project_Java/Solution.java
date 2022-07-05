import java.util.*;

public class Solution {
    public String decodeMessage(String key, String message) {
        // 3ms
        char[] dic = new char[26];
        int i = 0;
        for (char ch : key.toCharArray()) {
            if (i < 26 && ch != ' ' && dic[ch - 'a'] == 0) {
                dic[ch - 'a'] = (char)('a' + i);
                i++;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char ch : message.toCharArray()) {
            if (ch == ' ') {
                sb.append(" ");
            } else {
                sb.append(dic[ch - 'a']);
            }
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").split(",");
        String key = flds[0];
        String message = flds[1];
        System.out.println("key = \"" + key + "\", message = \"" + message + "\"");

        long start = System.currentTimeMillis();

        String result = decodeMessage(key, message);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
