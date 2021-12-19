import java.util.*;

public class Solution {
    public int countWords(String[] words1, String[] words2) {
        // 5ms
        HashMap<String, Integer> dic1 = new HashMap<>();
        HashMap<String, Integer> dic2 = new HashMap<>();

        for (String word : words1) {
            dic1.put(word, dic1.getOrDefault(word, 0) + 1);
        }

        for (String word : words2) {
            dic2.put(word, dic2.getOrDefault(word, 0) + 1);
        }

        int ans = 0;
        for (String key : dic1.keySet()) {
            if (dic1.get(key) == 1 && dic1.get(key) == dic2.get(key)) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String[] word1 = flds[0].split(","), word2 = flds[1].split(",");
        Mylib ml = new Mylib();
        System.out.println("word1 = " + ml.stringArrayToString(word1) + ", word2 = " + ml.stringArrayToString(word2));

        long start = System.currentTimeMillis();

        int result = countWords(word1, word2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
