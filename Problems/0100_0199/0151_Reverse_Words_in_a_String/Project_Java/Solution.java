import java.util.*;

public class Solution {
    public String reverseWords(String s) {
        // 1ms
        if (s == null || s.length() == 0)
            return s;

        String[] words = s.split(" ");
        StringBuilder results = new StringBuilder();

        for (int i = words.length - 1; i >= 0; i--)
            if (!words[i].isEmpty())
            results.append(words[i]).append(" ");

        if (results.length() > 1)
            results.deleteCharAt(results.length() - 1);
        return results.toString();
    }

    public String reverseWords2(String s) {
        // 6ms
        String[] words = s.trim().split(" +");
        StringBuffer results = new StringBuffer();
 
        results.append(words[words.length - 1]);
        for (int i = words.length - 2; i >= 0; i--) {
            results.append(" " + words[i]);
        }
 
        return results.toString();
    }

    public String reverseWords3(String s) {
        // 7ms
        String[] words = s.trim().split(" +");
        Collections.reverse(Arrays.asList(words));
        return String.join(" ", words);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String s = args.replace("\"", "").replace("[", "").replace("]", "");
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        String result = reverseWords(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
