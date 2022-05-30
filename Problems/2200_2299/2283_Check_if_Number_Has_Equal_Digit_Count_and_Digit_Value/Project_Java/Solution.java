import java.util.*;

public class Solution {
    public boolean digitCount(String num) {
        // 1ms
        int[] cnt = new int[10];
        for (int i = 0; i < num.length(); i++) {
            cnt[num.charAt(i) - '0']++;
        }
        for (int i = 0; i < num.length(); i++) {
            if (cnt[i] != num.charAt(i) - '0') {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String num = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("num = " + num);

        long start = System.currentTimeMillis();

        boolean result = digitCount(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
