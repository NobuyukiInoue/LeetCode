import java.util.*;

public class Solution {
    public boolean isValid_1liner(String word) {
        // 10ms
		return word.matches("(?i)(?=^.*[b-df-hj-np-tv-z])(?=.*[aieou])^[a-z0-9]{3,}$");
    }

    public boolean isValid(String word) {
        // 1ms
        if (word.length() < 3) {
            return false;
        }
        boolean isVowel = false;
        boolean isConsonant = false;
        for (char ch : word.toCharArray()) {
            if (!Character.isLetterOrDigit(ch)) {
                return false;
            }
            if ("aeiouAEIOU".indexOf(ch) != -1) {
                isVowel = true;
            } else if ("aeiouAEIOU".indexOf(ch) == -1 && Character.isAlphabetic(ch)) {
                isConsonant = true;
            }
        }
        return isVowel && isConsonant;
    }

    public void Main(String temp) {
        String word = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("word = \"" + word + "\"");

        long start = System.currentTimeMillis();

        boolean result = isValid(word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
