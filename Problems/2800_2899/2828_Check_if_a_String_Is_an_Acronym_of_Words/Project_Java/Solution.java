import java.util.*;

public class Solution {
    public boolean isAcronym(List<String> words, String s) {
        // 1ms
        if (words.size() != s.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            if (words.get(i).charAt(0) != s.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    public boolean isAcronym2(List<String> words, String s) {
        // 2ms
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            sb.append(word.charAt(0));
        }
        return sb.toString().equals(s);
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        String[] temp_words = flds[0].split(",");

        Mylib ml = new Mylib();
        List<String> words = Arrays.asList(temp_words);
       
        String s = flds[1];

        System.out.println("words = " + ml.listStringArrayToString(words) + ", s = '" + s + "'");
        long start = System.currentTimeMillis();

        boolean result = isAcronym(words, s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
