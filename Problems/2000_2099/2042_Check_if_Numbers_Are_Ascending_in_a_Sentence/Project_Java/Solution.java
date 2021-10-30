import java.util.*;

public class Solution {
    public boolean areNumbersAscending2(String s) {
        // 1ms
        int length = s.length();
        int val = 0;
        int last = -1;
        int idx = 0;
        while (idx < length) {
            char c = s.charAt(idx);
            if (c >= '0' && c <= '9') {
                int current = c - '0';
                val = val * 10 + current;              
            } else if (val != 0) {
                if (val <= last) {
                    return false;
                }
                last = val;
                val = 0;
            }
            idx++;
        }
        return val == 0 || val > last;
    }

    public boolean areNumbersAscending(String s) {
        // 12ms
        String[] words = s.split(" ");
        int prev = -1;
        for (String word : words) {
            if (word.matches("\\d+")) {
                int cur = Integer.parseInt(word);
                if (cur > prev) {
                    prev = cur;
                } else {
                    return false;
                }
            }
        }
        return true;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        Boolean result = areNumbersAscending(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
