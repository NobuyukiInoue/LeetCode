import java.util.*;

public class Solution {
    public int maxVowels(String s, int k) {
        // 8ms
        int count = 0;
        for (int i = 0;  i < k; i++) {
            if (i >= s.length())
                break;
            if (isVowel(s.charAt(i)))
                count++;
        }

        int maxCount = count;
        for (int i = k; i < s.length(); i++) {
            if (isVowel(s.charAt(i - k)))
                count--;
            if (isVowel(s.charAt(i)))
                count++;
            if (count > maxCount)
                maxCount = count;
        }

        return maxCount;
    }

    private boolean isVowel(char c) {
        if ((c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'))
            return true;
        return false;
    }

    public int maxVowels2(String s, int k) {
        //12ms
        int count = 0;
        String targetChars = "aeiou";

        for (int i = 0;  i < k; i++) {
            if (i >= s.length())
                break;
            if (targetChars.indexOf(s.charAt(i)) >= 0)
                count++;
        }

        int maxCount = count;

        for (int i = k; i < s.length(); i++) {
            if (targetChars.indexOf(s.charAt(i - k)) >= 0)
                count--;
            if (targetChars.indexOf(s.charAt(i)) >= 0)
                count++;
            if (count > maxCount)
                maxCount = count;
        }

        return maxCount;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0].replace("\"", "");
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = \"" + s + "\", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = maxVowels(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
