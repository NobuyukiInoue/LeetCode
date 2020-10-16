import java.util.*;

public class Solution {
    public String reorderSpaces2(String text) {
        // 6ms
        String[] words = text.trim().split("\\s+");
        int cnt = words.length;
        int spaces = text.chars().map(c -> c == ' ' ? 1 : 0).sum();
        int gap = cnt <= 1 ? 0 : spaces / (cnt - 1); 
        int trailingSpaces = gap == 0 ? spaces : spaces % (cnt - 1);
        return String.join(" ".repeat(gap), words) + " ".repeat(trailingSpaces);
    }

    public String reorderSpaces(String text) {
        // 1ms
        char[] next = new char[text.length()];
        int N = text.length();
        char[] b = text.toCharArray();
        int spCnt = 0;
        int wcnt = 0;
        List<Integer> idx = new ArrayList<Integer>();

        for (int i = 0; i < N; i++) {
            if (b[i] == ' ') {
                spCnt++;
            }
            if ((i > 0 && b[i - 1] == ' ' && b[i] != ' ') || (i == 0 && b[i] != ' ')) {
                wcnt++;
                idx.add(i);
            }
        }
        int sp = wcnt>1 ? spCnt / (wcnt-1): 0;
        int leftOver = wcnt > 1 ? spCnt % (wcnt-1): 0;
        int j = 0;

        Arrays.fill(next, ' ');
        for (int i = 0; i < idx.size(); i++) {
            int s = idx.get(i);
            while (s < N && b[s] != ' ') {
                next[j++] = b[s++];
            }
            j += sp;
        }
        return new String(next);
    }

    public void Main(String temp) {
        String text = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("text = " + text);

        long start = System.currentTimeMillis();

        String result = reorderSpaces(text);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
