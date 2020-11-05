import java.util.*;

public class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        // 0ms
        String[] words = sentence.split(" ");
        int len_searchWord = searchWord.length();

        for (int i = 0; i < words.length; i++) {
            if (words[i].length() >= len_searchWord) {
                if (searchWord.equals(words[i].substring(0, len_searchWord))) {
                    return i + 1;
                }
            }
        }

        return -1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String sentence = flds[0];
        String searchWord = flds[1];
        System.out.println("sentence = \"" + sentence + "\", searchWord = \"" + searchWord + "\"");

        long start = System.currentTimeMillis();

        int result = isPrefixOfWord(sentence, searchWord);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
