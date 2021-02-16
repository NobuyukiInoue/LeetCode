import java.util.*;

public class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        // 31ms
        int res = 0;
        HashSet<String> sub = new HashSet<>();
        HashSet<String> nonsub = new HashSet<>();
        for (String word : words) {
            if (sub.contains(word)) {
                res++;
                continue;
            }
            if (nonsub.contains(word)) {
                continue;
            }
            if (isSub(S, word)) {
                sub.add(word);
                res++;
            } else {
                nonsub.add(word);
            }
        }
        return res;
    }
    
    private boolean isSub(String S, String word){
        int index = -1;
        for (char ch : word.toCharArray()) {
            index = S.indexOf(ch, index + 1);
            if (index == -1)
                return false;
        }
        return true;
    }

    public int numMatchingSubseq2(String S, String[] words) {
        // 1137ms
        int res = 0;
        for (String word : words) {
            int i = 0;
            boolean match = true;
            for (char ch : word.toCharArray()) {
                i = S.indexOf(Character.toString(ch), i) + 1;
                if (i == 0) {
                    match = false;
                    break;
                }
            }
            if (match) {
                res++;
            }
        }
        return res;
    }

    public int numMatchingSubseq3(String S, String[] words) {
        // 1176ms
        int res = 0;
        for (String word : words) {
            int i = 0;
            boolean match = true;
            for (int pos = 0; pos < word.length(); pos++) {
                i = S.indexOf(word.substring(pos, pos + 1), i) + 1;
                if (i == 0) {
                    match = false;
                    break;
                }
            }
            if (match) {
                res++;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String S = flds[0];
        String[] words = flds[1].split(",");

        Mylib ml = new Mylib();
        System.out.println("S = " + S);
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        int result = numMatchingSubseq(S, words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
