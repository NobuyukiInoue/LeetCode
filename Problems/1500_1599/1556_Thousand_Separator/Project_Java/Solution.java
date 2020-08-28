import java.util.*;

public class Solution {
    public String thousandSeparator(int n) {
        // 0ms
        String num = Integer.toString(n);
        StringBuilder sb = new StringBuilder();
        for (int i = num.length(); i > 0; i -= 3) {
            if (sb.length() > 0)
                sb.insert(0, ".");
            sb.insert(0, num.substring(Math.max(0, i - 3), i));
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        String result = thousandSeparator(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
