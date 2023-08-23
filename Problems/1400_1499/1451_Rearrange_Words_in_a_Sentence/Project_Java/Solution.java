import java.util.*;

public class Solution {
    public String arrangeWords(String text) {
        // 20ms
        String words[] = text.split(" ");
        Arrays.sort(words, (str1, str2) -> str1.length() - str2.length());
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            if (i == 0) {
                ans.append(words[i].substring(0,1).toUpperCase() + words[i].substring(1));
            } else {
                ans.append(words[i].toLowerCase());
            }
            ans.append(" ");
        }
        return ans.toString().trim();
    }

    public String arrangeWords2(String text) {
        // 22ms
        String[] words = text.split(" ");
        Arrays.sort(words, (str1, str2) -> str1.length() - str2.length());
        StringBuilder sb = new StringBuilder();
        sb.append(words[0].substring(0,1).toUpperCase() + words[0].substring(1));
        for (int i = 1; i < words.length; i++){
            sb.append(" " + words[i].toLowerCase());
        }
        return sb.toString().trim();
    }

    public void Main(String temp) {
        String text = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("text = \"" + text + "\"");

        long start = System.currentTimeMillis();

        String result = arrangeWords(text);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
