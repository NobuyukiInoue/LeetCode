import java.util.*;

public class Solution {
    public String findValidPair(String s) {
        // 3ms
        Map<Character, Integer> cnts = new HashMap<Character,Integer>();
        char[] arr_s = s.toCharArray();
        for (char ch : arr_s) {
            cnts.put(ch, cnts.getOrDefault(ch,0) + 1);
        }
        for (int i = 0; i < s.length() - 1; i++) {
            if (arr_s[i] != arr_s[i + 1] 
            && cnts.get(arr_s[i]) == (arr_s[i] - '0')
            && cnts.get(arr_s[i + 1]) == (arr_s[i + 1] - '0')) {
                return s.substring(i, i + 2);
            }
        }
        return "";
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        String result = findValidPair(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
