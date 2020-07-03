import java.util.*;

public class Solution {
    public String convert(String s, int numRows) {
        // 2ms
        if(numRows <= 1)
            return s;

        var sb = new StringBuilder(s.length()); 
        int lap = numRows * 2 - 2;
        for (int r = 0; r < numRows && r < s.length(); r++) {
            sb.append(s.charAt(r));

            int d = r == 0 || r == numRows - 1 ? lap * 2 : lap;
            int m = r == numRows - 1 ? lap * 2 : lap;
            int c = r;

            while(true) {
                c = m - c;
                m += d;
                if(c >= s.length())
                    break;
                sb.append(s.charAt(c));
            }
        }

        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String s = flds[0];
        int numRows = Integer.parseInt(flds[1]);
        System.out.println("s = " + flds[0] + ", numRows = " + Integer.toString(numRows));

        long start = System.currentTimeMillis();

        String result = convert(s, numRows);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
