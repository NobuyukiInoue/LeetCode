import java.util.*;

public class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        // 1ms
        int res = 0;
        String vowel = "aeiou";
        for (int i = left; i <= right; i++) {
            if (vowel.indexOf(words[i].charAt(0)) != -1 &&
                vowel.indexOf(words[i].charAt(words[i].length() - 1)) != -1) {
                res++;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        String[] words = flds[0].split(",");
        int left = Integer.parseInt(flds[1]);
        int right = Integer.parseInt(flds[2]);

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words) + ", left = " + left + ", right = " + right);
        long start = System.currentTimeMillis();

        int result = vowelStrings(words, left, right);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
