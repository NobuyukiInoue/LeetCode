import java.util.*;

public class Solution {
    public boolean makeEqual(String[] words) {
        // 2ms
        int[] chars = new int[26];
        for (String word : words) {
            for (char ch : word.toCharArray()) {
                chars[ch - 'a']++;
            }
        }
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] % words.length != 0) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        boolean result = makeEqual(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
