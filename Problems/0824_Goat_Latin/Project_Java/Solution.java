import java.util.*;

public class Solution {
    public String toGoatLatin2(String S) {
        // 20ms
        Set<Character> vowel = new HashSet<Character>();

        for (char c : "aeiouAEIOU".toCharArray())
            vowel.add(c);

        String res = "";
        int i = 0, j = 0;

        for (String w : S.split("\\s")) {
            res += ' ' + (vowel.contains(w.charAt(0)) ? w : w.substring(1) + w.charAt(0)) + "ma";
            for (j = 0, ++i; j < i; ++j)
                res += "a";
        };

        return res.substring(1);
    }

    public String toGoatLatin(String S) {
        // 2ms
        StringBuilder result = new StringBuilder();
        StringBuilder lastAppendStr = new StringBuilder();
        String[] words = S.split(" ");
        Set<Character> lowerVowels = new HashSet<>();
        lowerVowels.add('a');
        lowerVowels.add('e');
        lowerVowels.add('i');
        lowerVowels.add('o');
        lowerVowels.add('u');

        for (String word : words) {
            char firstChar = word.charAt(0);
            if (lowerVowels.contains(Character.toLowerCase(firstChar))) {
                result.append(word);
            } else {
                result.append(word.substring(1)).append(firstChar);
            }
            result.append("ma").append(lastAppendStr).append("a ");
            lastAppendStr.append("a");
        }
        
        return result.toString().trim();
    }

    public void Main(String temp) {
        String S = temp.replace("\"", "").replace("[", "").replace("]", "").trim();

        System.out.println("S = " + S);

        long start = System.currentTimeMillis();
        
        String result = toGoatLatin(S);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
