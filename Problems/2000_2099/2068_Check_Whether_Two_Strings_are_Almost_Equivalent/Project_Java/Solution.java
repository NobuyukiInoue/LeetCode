import java.util.*;

public class Solution {
    public boolean checkAlmostEquivalent1(String word1, String word2) {
        // 0ms
        int i = word1.length();
        int []frequency = new int[26];
        while (--i >= 0) {
            frequency[word1.charAt(i) - 'a']++;
            frequency[word2.charAt(i) - 'a']--;
        }
        while (++i < 26) {
            if(frequency[i] > 3|| frequency[i] < -3) {
                return false;
            }
        }
        return true;
    }

    public boolean checkAlmostEquivalent(String word1, String word2) {
        // 0ms
        int[] count1 = getCount(word1);
        int[] count2 = getCount(word2);
        
        for(int i = 0; i < 26; i++){
            if(Math.abs(count1[i] - count2[i]) > 3){
                return false;
            }
        }
        
        return true;
    }
    
    private int[] getCount(String s){
        int[] count = new int[26];
        int i, n = s.length();
        
        for(i = 0; i < n; i++){
            count[s.charAt(i) - 'a']++;
        }
        
        return count;
    }

    public boolean checkAlmostEquivalent3(String word1, String word2) {
        // 3ms
        HashMap<Character, Integer> cnt1 = new HashMap<>();
        HashMap<Character, Integer> cnt2 = new HashMap<>();
        for (char ch : word1.toCharArray()) {
            cnt1.put(ch, cnt1.getOrDefault(ch, 0) + 1);
        }
        for (char ch : word2.toCharArray()) {
            cnt2.put(ch, cnt2.getOrDefault(ch, 0) + 1);
        }
        for (char key : cnt1.keySet()) {
            if (Math.abs(cnt1.get(key) - cnt2.getOrDefault(key, 0)) > 3) {
                return false;
            }
        }
        for (char key : cnt2.keySet()) {
            if (Math.abs(cnt1.getOrDefault(key, 0) - cnt2.get(key)) > 3) {
                return false;
            }
        }
        return true;
    }

    public boolean checkAlmostEquivalent4(String word1, String word2) {
        // 4ms
        int[] counts = new int[26];
        word1.chars().forEach(c -> counts[c - 'a']++);
        word2.chars().forEach(c -> counts[c - 'a']--);
        return Arrays.stream(counts).allMatch(c -> Math.abs(c) <= 3);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String word1 = flds[0], word2 = flds[1];
        System.out.println("word1 = " + word1 + ", word2 = " + word2);

        long start = System.currentTimeMillis();

        boolean result = checkAlmostEquivalent(word1, word2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
