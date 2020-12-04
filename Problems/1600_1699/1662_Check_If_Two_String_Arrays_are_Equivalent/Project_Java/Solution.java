import java.util.*;

public class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        // 0ms
        StringBuilder w1 = new StringBuilder(word1[0]);
        StringBuilder w2 = new StringBuilder(word2[0]);

        for (int i = 1; i < word1.length; i++)
            w1.append(word1[i]);
        for (int i = 1; i < word2.length; i++)
            w2.append(word2[i]);

        return w1.toString().equals(w2.toString());
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String[] word1 = flds[0].split(",");
        String[] word2 = flds[1].split(",");
        
        Mylib ml = new Mylib();
        System.out.println("word1 = " + ml.stringArrayToString(word1));
        System.out.println("word2 = " + ml.stringArrayToString(word2));

        long start = System.currentTimeMillis();

        boolean result = arrayStringsAreEqual(word1, word2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
