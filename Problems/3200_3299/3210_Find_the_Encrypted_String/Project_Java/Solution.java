import java.util.*;

public class Solution {
    public String getEncryptedString(String s, int k) {
        // 1ms
        k %= s.length();
        return s.substring(k) + s.substring(0, k);
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0].replace("\"", "");
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = \"" + s + "\", k = " + k);

        long start = System.currentTimeMillis();

        String result = getEncryptedString(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
