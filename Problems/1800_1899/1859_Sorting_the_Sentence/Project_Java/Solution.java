import java.util.*;
import java.util.stream.Collectors;

public class Solution {
    public String sortSentence(String s) {
        // 1ms
        String[] words = s.split(" ");
        String[] flds = new String[words.length];
        for (String word : words) {
            int wordLen = word.length();
            flds[word.charAt(wordLen - 1) - '0' - 1] = word.substring(0, wordLen - 1);
        }
        return String.join(" ", flds);
    }

    public String sortSentence2(String s) {
        // 5ms
        return Arrays.stream(s.split(" ")).sorted(Comparator.comparingInt(word -> word.charAt(word.length() - 1))).map(word -> word.substring(0, word.length() - 1)).collect(Collectors.joining(" "));
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = sortSentence(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
