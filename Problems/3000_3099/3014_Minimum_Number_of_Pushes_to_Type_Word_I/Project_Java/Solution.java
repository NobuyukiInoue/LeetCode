import java.util.*;

public class Solution {
    public int minimumPushes(String word) {
        // 0ms
        int n = word.length(), row = 1, ans = 0;
        for (int div = n / 8; div > 0; div--) {
            ans += (row++)*8;
        }
        return ans + (n%8)*row;
    }

    public void Main(String temp) {
        String word = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("word = \"" + word + "\"");

        long start = System.currentTimeMillis();

        int result = minimumPushes(word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
