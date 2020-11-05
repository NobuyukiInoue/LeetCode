import java.util.*;

public class Solution {
    public int balancedStringSplit(String s) {
        // 0ms
        int res = 0, cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'L')
                cnt++;
            else
                cnt--;
            if (cnt == 0)
                res++;
        }
        return res;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = balancedStringSplit(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
