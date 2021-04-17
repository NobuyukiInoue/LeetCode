import java.util.*;

public class Solution {
    public String truncateSentence(String s, int k) {
        // 0ms
        int n = 0;
        int t = s.length();
        for(int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ')
                n++;
            if (n == k) {
                t = i;
                break;
            }
        }
        return s.substring(0, t);
    }

    public String truncateSentence2(String s, int k) {
        // 2ms
        return String.join(" ", Arrays.copyOfRange(s.split(" "), 0, k));
    }

    public String truncateSentence3(String s, int k) {
        // 2ms
        String[] flds = s.split(" ");
        if (k < 1)
            return "";
        StringBuilder sb = new StringBuilder(flds[0]);
        for (int i = 1; i < k; i++) {
            sb.append(" " + flds[i]);
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = \"" + s + "\", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        String result = truncateSentence(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
