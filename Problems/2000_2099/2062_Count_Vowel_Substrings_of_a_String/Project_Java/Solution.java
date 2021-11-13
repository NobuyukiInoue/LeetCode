import java.util.*;

public class Solution {
    public int countVowelSubstrings(String word) {
        // 2ms
        Map<Character, Integer> vowel = new HashMap<>();
        int start = 0;
        int end = start;
        int count = 0;
        while (start < word.length()) {
            while (start < word.length() && !isVowel(word.charAt(start))) {
                start++;
            }
            end = start;
            while (end < word.length() && isVowel(word.charAt(end))) {
                vowel.put(word.charAt(end), end);
                if (vowel.size() == 5) {
                    int temp = count(start, vowel);
                    count += temp;
                }
                end++;
            }
            vowel.clear();
            start = end + 1;
        }
        return count;
    }
    
    private int count(int s, Map<Character, Integer> map) {
        int last = Integer.MAX_VALUE;
        for (int v : map.values()) {
            last = Math.min(last, v);
        }
        return last - s + 1;
    }
    
    private boolean isVowel(char c) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c== 'u') {
            return true;
        }
        return false;
    }

    public int countVowelSubstrings2(String word) {
        // 11ms
        Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u');
        Set<Character> curr = new HashSet<>();
        int count = 0;
        char[] w = word.toCharArray();
        for (int i = 0; i < w.length; i++, curr.clear()) {
            for (int j = i; j < w.length && vowels.contains(w[j]); j++) {
                curr.add(w[j]);
                count += curr.size() == vowels.size() ? 1 : 0;
            }
        }
        return count;
    }

    public void Main(String temp) {
        String word = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("word = " + word);

        long start = System.currentTimeMillis();

        int result = countVowelSubstrings(word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
