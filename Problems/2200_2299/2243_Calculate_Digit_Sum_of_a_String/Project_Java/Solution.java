import java.util.*;

public class Solution {
    public String digitSum(String s, int k) {
        // 1ms
        while (s.length() > k) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < s.length(); i += k) {
                int sm = 0;
                for (int j = i; j < i + k && j < s.length(); j++) {
                    sm += s.charAt(j) - '0';
                }
                sb = sb.append(Integer.toString(sm));
            }
            s = sb.toString();
        }
        return s;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = " + s + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        String result = digitSum(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
