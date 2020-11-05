import java.util.*;

public class Solution {
    public int maxScore(String s) {
        // 1ms
        int zeroCount = 0;
        int oneCount = 0;
        int max = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1')
                oneCount++;
        }
        
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '0')
                zeroCount++;
            else
                oneCount--;
            if (zeroCount+oneCount > max)
                max = zeroCount + oneCount;
        }
        
        return max;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = maxScore(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
