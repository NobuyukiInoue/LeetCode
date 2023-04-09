import java.util.*;

public class Solution {
    public int findTheLongestBalancedSubstring1(String s) {
        // 5ms
        int res = 0;
        String temp = "01";
        while (temp.length() <= s.length()) {
            if (s.indexOf(temp) >= 0) {
                res = temp.length();
            }
            temp = "0" + temp + "1";
        }
        return res;
    }

    public int findTheLongestBalancedSubstring(String s) {
        // 2ms
        int max = 0;
        for (int i = 0; i < s.length(); ){
            int z = 0, o = 0;
            while (i < s.length() && s.charAt(i) == '0') {
                z++;
                i++;
            }
            while (i < s.length() && s.charAt(i) =='1' && z > o){
                o++;
                i++;  
                max = Math.max(max, o*2);
            } 
            while (i < s.length() && s.charAt(i) == '1') i++;
        }
        return max;
    }

    public void Main(String temp) {
        String sentence = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("sentence = " + sentence);

        long start = System.currentTimeMillis();

        int result = findTheLongestBalancedSubstring(sentence);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
