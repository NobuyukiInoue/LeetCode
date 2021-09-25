import java.util.*;

public class Solution {
    public int longestStrChain(String[] words) {
        // 28ms
        Arrays.sort(words,  new Comparator<String>(){
            public int compare(String s0, String s1) {
                return s0.length() - s1.length();
            }
        });
        Map<String, Integer> map = new HashMap<>();
        int res = 0;
        for (String word : words) {
            int cur = 1;
            StringBuilder sb = new StringBuilder(word);
            int N = word.length();
            for (int i = 0; i < N; i++) {
                char ch = sb.charAt(i);
                sb.deleteCharAt(i);
                String possible = sb.toString();
                if (map.containsKey(possible)) {
                    cur = Math.max(cur, map.get(possible) + 1);
                }
                if (i < N - 1)
                    sb.insert(i, ch);
            }
            map.put(word, cur);
            res = Math.max(res, cur);
        }
        return res;
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        int result = longestStrChain(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
