import java.util.*;

public class Solution {
    public int titleToNumber(String s) {
        int result = 0;
        for (int i = 0; i < s.length(); i++)
            result = result * 26 + (s.charAt(i) - 'A' + 1);
        return result;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        int result = titleToNumber(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
