import java.util.*;

public class Solution {
    public boolean areOccurrencesEqual2(String s) {
        // 4ms
        HashMap<Character, Integer> dic = new HashMap<>();
        for (char ch : s.toCharArray()) {
            dic.put(ch, dic.getOrDefault(ch, 0) + 1);
        }
        int preCnt = dic.get(s.charAt(0));
        for (Integer cnt : dic.values()) {
            if (cnt != preCnt) {
                return false;
            }
        }
        return true;
    }

    public boolean areOccurrencesEqual(String s) {
        // 1ms
        int[] count = new int[26];
        int i, N = s.length();
        
        for (i = 0; i < N; i++) {
            count[s.charAt(i) - 'a']++;
        }
        
        int expected = 0;
        for (i = 0; i < 26; i++) {
            if(count[i] != 0){
                expected = count[i];
                break;
            }
        }
        
        for (; i < 26; i++) {
            if (count[i] != 0 && count[i] != expected)
                return false;
        }
        
        return true;
    }

    public boolean areOccurrencesEqual3(String s) {
        // 5ms
        int cnt[] = new int[26];
        s.chars().forEach(ch -> ++cnt[ch - 'a']);
        int m_cnt = Arrays.stream(cnt).max().getAsInt();
        return Arrays.stream(cnt).filter(c -> c > 0).allMatch(c -> c == m_cnt);
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        boolean result = areOccurrencesEqual(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
