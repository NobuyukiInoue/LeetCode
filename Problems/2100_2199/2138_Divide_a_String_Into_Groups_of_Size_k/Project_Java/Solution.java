import java.util.*;

public class Solution {
    public String[] divideString(String s, int k, char fill) {
        // 2ms
        String[] res = new String[(int)Math.ceil((double)s.length() / (double)k)];
        int pos, i;
        for (pos = 0, i = 0; pos + k <= s.length(); i++, pos += k) {
            res[i] = s.substring(pos, pos + k);
        }
        if (pos < s.length()) {
            StringBuilder sb = new StringBuilder(s.substring(pos, s.length()));
            for (int j = sb.length(); j < k; j++) {
                sb.append(fill);
            }
            res[i] = sb.toString();
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        char fill = flds[2].charAt(0);
        System.out.println("s = " + s + ", k = " + Integer.toString(k) + ", fill = " + fill);

        long start = System.currentTimeMillis();

        String[] result = divideString(s, k, fill);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.stringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
