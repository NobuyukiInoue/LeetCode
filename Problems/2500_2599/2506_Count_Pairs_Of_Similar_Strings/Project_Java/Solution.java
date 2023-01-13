import java.util.*;

public class Solution {
    public int similarPairs(String[] words) {
        // 4ms
        Map<Integer, Integer> freq = new HashMap<>();
        for (String word : words) {
            freq.merge(convert(word), 1, Integer::sum);
        }
        int count = 0;
        for (int value : freq.values()) {
            count += value * (value - 1) / 2;
        }
        return count;
    }
    
    public int similarPairs_oneloop(String[] words) {
        // 4ms
        Map<Integer, Integer> freq = new HashMap<>();
        int ans = 0;
        for (String word : words) {
            int mask = convert(word);
            int current = freq.getOrDefault(mask, 0);
            ans += current;
            freq.put(mask, current + 1);
        }
        return ans;
    }

    private int convert(String word) {
        int n = 0;
        for (char ch : word.toCharArray()) {
            n |= 1 << (ch - 'a');
        }
        return n;
    }

    public void Main(String temp) {
        String[] words = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").split(",");
        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));
        long start = System.currentTimeMillis();

        int result = similarPairs(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
