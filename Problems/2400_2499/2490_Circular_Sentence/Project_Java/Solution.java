import java.util.*;

public class Solution {
    public boolean isCircularSentence(String sentence) {
        // 1ms
        String[] words = sentence.split(" ");
        if (words[0].charAt(0) != words[words.length - 1].charAt(words[words.length - 1].length() - 1)) {
            return false;
        }
        for (int i = 0; i < words.length - 1; i++) {
            if (words[i + 1].charAt(0) != words[i].charAt(words[i].length() - 1)) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String sentence = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("sentence = " + sentence);

        long start = System.currentTimeMillis();

        boolean result = isCircularSentence(sentence);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
