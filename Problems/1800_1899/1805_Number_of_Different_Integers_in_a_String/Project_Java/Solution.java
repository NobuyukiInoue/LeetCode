import java.util.*;

public class Solution {
    public int numDifferentIntegers(String word) {
        // 1ms
        var set = new HashSet<String>();
        int i = 0;
        int len = word.length();
        while (i < len) {
            var let = word.charAt(i);
            if (Character.isDigit(let)) {
                int end = i;
                while (end < len && Character.isDigit(word.charAt(end))) {
                    end++;
                }
                while (i < end && word.charAt(i) == '0') {
                    i++;
                }
                set.add(word.substring(i, end));
                i = end + 1;
            } else {
                i++;
            }
        }
        return set.size();
    }

    public void Main(String temp) {
        String word = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("word = " + word);

        long start = System.currentTimeMillis();

        int result = numDifferentIntegers(word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
