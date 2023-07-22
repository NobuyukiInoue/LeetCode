import java.util.*;

public class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        // 3ms
        int ans = 0;
        Set<String> wordSet = new HashSet<>();
        for (String word : words) {
            StringBuilder sb = new StringBuilder(word);
            String reversedWord = sb.reverse().toString();
            if (wordSet.contains(reversedWord)) {
                ans++;
            }
            wordSet.add(word);
        }
        return ans;
    }

    public int maximumNumberOfStringPairs_use_map(String[] words) {
        // 4ms
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            String rev = new StringBuilder(word).reverse().toString();
            if (map.containsKey(rev)) {
                map.put(rev, map.get(rev) + 1);
            } else {
                map.put(word,0);
            }
        }
        int ans = 0;
        for (int val : map.values()) {
            ans += val;
        }
        return ans;
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        int result = maximumNumberOfStringPairs(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
