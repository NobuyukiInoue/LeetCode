import java.util.*;

public class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // 5ms
        Map<String, Integer> map = new HashMap<>();
        for (String word: words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }

        List<String>[] freq = new List[words.length + 1];
        for (String key: map.keySet()) {
            int f = map.get(key);
            if (freq[f] == null)
                freq[f] = new ArrayList<String>();
            freq[f].add(key);
        }

        List<String> res = new ArrayList<>();
        for (int i = freq.length - 1; i >= 0 && res.size() < k; i--) {
            if (freq[i] != null) {
                Collections.sort(freq[i]);
                res.addAll(freq[i]);
            }
        }

        return res.size() == k? res: res.subList(0, k);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String[] words = flds[0].split(",");
        int k = Integer.parseInt(flds[1]);

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        List<String> result = topKFrequent(words, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
