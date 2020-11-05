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

    public void Main(String arg) {
        String[] flds = arg.replace("\"", "").trim().split("\\],\\[\\[");
        String[] ope = flds[0].replace("[", "").replace("]", "").split(",");
        String[] words = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        System.out.println("ope[] = " + ml.stringArrayToString(ope));
        System.out.println("words[] = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        WordDictionary_Main(ope, words);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
