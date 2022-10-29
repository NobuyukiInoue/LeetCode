import java.util.*;

public class Solution {
    public boolean equalFrequency(String word) {
        // 0ms
        int[] freq = new int[26];
        for (char ch : word.toCharArray()) {
            freq[ch -  'a']++;
        }
        for (char ch:word.toCharArray()){
            freq[ch - 'a']--;
            if (check_allSame(freq)) {
                return true;
            }
            freq[ch - 'a']++;
        }
        return false;
    }

    private boolean check_allSame(int freq[])
    {
        int same = 0;
        int i;
        for (i = 0; i < freq.length; i++) {
            if (freq[i] > 0) {
                same = freq[i];
                break;
            }
        }
        for (int j = i + 1; j < freq.length; j++) {
            if (freq[j] > 0 && freq[j] != same) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String word = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("word = " + word);

        long start = System.currentTimeMillis();

        boolean result = equalFrequency(word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
