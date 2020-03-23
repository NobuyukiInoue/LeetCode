import java.util.*;

public class Solution {
    public String generateTheString(int n) {
        // 0ms
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n - 1; i++) {
            sb.append('a');
        }

        if (n % 2 == 0)
            return sb.append('b').toString();
        else
            return sb.append('a').toString();
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        String result = generateTheString(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
