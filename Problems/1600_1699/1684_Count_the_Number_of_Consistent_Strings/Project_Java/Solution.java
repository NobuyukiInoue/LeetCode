import java.util.*;

public class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        // 5ms
        boolean [] map = new boolean[26];
        int count = 0;

        for (char ch: allowed.toCharArray()) {
            map[ch - 'a'] = true;
        }
        for (String word : words) {
            boolean isConsistent = true;
            for (char ch: word.toCharArray()) {
                if (map[ch - 'a'] == false ) {
                    isConsistent = false;
                    break;
                }
            }
            if (isConsistent == true) {
                count++;
            }
        }
        return count;
    }

    public int countConsistentStrings2(String allowed, String[] words) {
        // 12ms
        int count = 0;
        char[] allowedLetters = allowed.toCharArray();
        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                if (!contains(allowedLetters, word.charAt(i))) {
                    count++;
                    break;
                }
            }
        }
        return words.length - count;
    }

    private boolean contains(char[] letters, char target) {
        for (char letter : letters) {
            if (target == letter) {
                return true;
            }
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String allowed = flds[0];
        String[] words = flds[1].split(",");

        Mylib ml = new Mylib();
        System.out.println("allowed = " + allowed);
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        int result = countConsistentStrings(allowed, words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
