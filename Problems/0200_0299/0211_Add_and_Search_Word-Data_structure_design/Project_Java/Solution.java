import java.util.*;

public class Solution {

    private void WordDictionary_Main(String[] ope, String[] words) {
        if (ope.length != words.length)
            return;
        if (ope.length <= 0 || words.length <= 0)
            return;

        WordDictionary WordDictionary = new WordDictionary();

        for (int i = 0; i < ope.length; i++) {
            if (ope[i].equals("addWord")) {
                WordDictionary.addWord(words[i]);
                System.out.println("addWord(" +  words[i] + ")");

            } else if (ope[i].equals("search")) {
                boolean res = WordDictionary.search(words[i]);
                System.out.println("search(" +  words[i] + ") ... " + Boolean.toString(res));

            }
        }
    }

    public String output_str_array(String[] words) {
        String result = "[";

        for (int i = 0; i < words.length; i++) {
            if (i == 0) {
                result += "\"" + words[i] + "\"";
            } else {
                result += ",\"" + words[i] + "\"";
            }
        }

        return result + "]";
    }

    public void Main(String arg) {
        String[] flds = arg.replace("\"", "").trim().split("\\],\\[\\[");
        String[] ope = flds[0].replace("[", "").replace("]", "").split(",");
        String[] words = flds[1].replace("]]]", "").split("\\],\\[");

        System.out.println("ope[] = " + output_str_array(ope));
        System.out.println("words[] = " + output_str_array(words));

        long start = System.currentTimeMillis();
        
        WordDictionary_Main(ope, words);
    
        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
