import java.util.*;

public class Solution {
    public String firstPalindrome(String[] words) {
        // 1ms
        for (String word : words) {
            if (check(word)) {
                return word;
            }
        }
        return "";
    }

    public static boolean check(String word) {
        int start = 0;
        int end = word.length() - 1;
        while (start < end) {
            if (word.charAt(start) != word.charAt(end)) {
                return false;
            } else {
                start++;
                end--;
            }
        }
        return true;
    }

    public String firstPalindrome2(String[] words) {
        // 2ms
        for (String word : words) {
            boolean isPalindrome = true;
            for (int i = 0; i < word.length()/2; i++) {
                if (word.charAt(i) != word.charAt(word.length() - 1 - i)) {
                    isPalindrome = false;
                    break;
                }
            }
            if (isPalindrome) {
                return word;
            }
        }
        return "";
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        String result = firstPalindrome(words);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
