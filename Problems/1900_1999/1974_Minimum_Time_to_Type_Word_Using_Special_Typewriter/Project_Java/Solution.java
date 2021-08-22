import java.util.*;

public class Solution {
    public int minTimeToType(String word) {
        // 0ms
        int cnt = word.length();
        char prev = 'a';
        for (char cur : word.toCharArray()) {
            int diff = Math.abs(cur - prev);
            cnt += Math.min(diff, 26 - diff);
            prev = cur;
        }
        return cnt;
    }

    public void Main(String temp) {
        String word = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("word = " + word);

        long start = System.currentTimeMillis();

        int result = minTimeToType(word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
