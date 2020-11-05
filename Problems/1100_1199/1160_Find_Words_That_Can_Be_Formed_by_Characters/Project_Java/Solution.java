import java.util.*;

public class Solution {
    public int countCharacters(String[] words, String chars) {
        // 3ms
        int total = 0;
        if (words==null || words.length==0)
            return total;
        int[] dict = new int[26];
        for(char ch : chars.toCharArray()) {
            dict[ch-'a']++;
        }
        for(String word : words) {
            boolean canForm = true;
            int[] arr = Arrays.copyOf(dict, dict.length);
            for(char ch : word.toCharArray()) {
                if(arr[ch-'a'] == 0) {
                    canForm = false;
                    break;
                } else {
                    arr[ch-'a']--;
                }
            }
            if (canForm)
                total += word.length();
        }
        return total;
    }

    public int countCharacters2(String[] words, String chars) {
        // 4ms
        int[] c = new int[128];
        for (char ch : chars.toCharArray()) {
            c[ch]++;
        }
        
        int res = 0;
        for (String s : words) {
            int[] c2 = Arrays.copyOf(c, 128);
            boolean valid = true;
            for (char ch : s.toCharArray()) {
                c2[ch]--;
                if (c2[ch] < 0) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                res+= s.length();
            } 
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds  = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String[] words = flds[0].split(",");
        String chars = flds[1];

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words) + ", chars = " + chars);

        long start = System.currentTimeMillis();
        
        int result = countCharacters(words, chars);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
