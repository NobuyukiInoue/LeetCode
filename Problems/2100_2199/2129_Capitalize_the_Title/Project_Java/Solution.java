import java.util.*;

public class Solution {
    public String capitalizeTitle(String title) {
        // 0ms
        int CASE_DIFF = 'a' - 'A';
        char[] ctitle = title.toCharArray();
        int ctitle_len = ctitle.length;
        for(int b = 0, i = 0; i <= ctitle_len; i++) {
            if (i == ctitle_len || ctitle[i] ==' '){
                if (i - b > 2) {
                    ctitle[b] -= CASE_DIFF;
                }
                b = i + 1;
            } else if(ctitle[i] < 'a') {
                ctitle[i] += CASE_DIFF;
            }
        }
        return new String(ctitle);
    }

    public String capitalizeTitle_sb(String title) {
        // 7ms
        StringBuilder sb = new StringBuilder();
        for (String word : title.split(" ")) {
            if (word.length() < 3) {
                sb.append(" " + word.toLowerCase());
            } else {
                word = word.toLowerCase();
                sb.append(" " + String.valueOf(word.charAt(0)).toUpperCase() + word.substring(1));
            }
        }
        return sb.toString().substring(1);
    }

    public void Main(String temp) {
        String title = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + title + "\"");

        long start = System.currentTimeMillis();

        String result = capitalizeTitle(title);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
