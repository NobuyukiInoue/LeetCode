import java.util.*;

public class Solution {
    public int maxRepeating(String sequence, String word) {
        // 0ms
        for (int i = sequence.length()/word.length(); i > 0; i--) {
            if (sequence.indexOf(word.repeat(i)) >= 0) {
                return i;
            }
        }
        return 0;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String sequence = flds[0];
        String word = flds[1];
        System.out.println("sequence = " + sequence);
        System.out.println("word = " + word);

        long start = System.currentTimeMillis();

        int result = maxRepeating(sequence, word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
