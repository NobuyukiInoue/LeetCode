import java.util.*;

public class Solution {
    public boolean sumGame(String num) {
        // 11ms - 28m
        int n = num.length();
        double res = 0;
        for (int i = 0; i < n; i++) {
            res += (i < n / 2 ? 1 : -1) * (num.charAt(i) == '?' ? 4.5 : num.charAt(i) - '0');
        }
        return res != 0;
    }

    public void Main(String temp) {
        String num = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("num = " + num);

        long start = System.currentTimeMillis();

        boolean result = sumGame(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
