import java.util.*;

public class Solution {
    public int numberOfSpecialChars(String word) {
        // 1ms
        int ans = 0;
        boolean[] cnts = new boolean[128];
        for (char ch : word.toCharArray()) {
            cnts[ch] = true;
        }
        for (int i = 'A'; i <= 'Z'; i++) {
            if (cnts[i] && cnts[i + 0x20]) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String word = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + word + "\"");

        long start = System.currentTimeMillis();

        int result = numberOfSpecialChars(word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
