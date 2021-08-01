import java.util.*;

public class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        // 2ms
        String[] words =text.split(" ");

        HashSet<Character> dic = new HashSet<>();
        for (char ch : brokenLetters.toCharArray()) {
            dic.add(ch);
        }

        int ans = 0;
        for (String word : words) {
            boolean used = false;
            for(char ch : word.toCharArray()){
                if (dic.contains(ch)){
                    used = true;
                    break;
                }
            }
            if (!used) {
                ans++;
            }
        }
        return ans;
    }

    public int canBeTypedWords2(String text, String brokenLetters) {
        // 2ms
        String[] words = text.split(" ");
        char[] brokenLettersChars = brokenLetters.toCharArray();
        int ans = 0;
        for (String word : words) {
            boolean used = false;
            for (char ch1 : word.toCharArray()) {
                for (char ch2 : brokenLettersChars) {
                    if (ch1 == ch2) {
                        used = true;
                        break;
                    }
                }
                if (used) {
                    break;
                }
            }
            if (!used) {
                ans++;
            }
        }
        return ans;
    }

    public int canBeTypedWords3(String text, String brokenLetters) {
        // 5ms
        return (int) Arrays.stream(text.split(" ")).filter(s -> s.chars().allMatch(c -> brokenLetters.indexOf(c) == -1)).count();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String text = flds[0];
        String brokenLetters = flds[1];
        System.out.println("text = " + text + ", brokenLetters = " + brokenLetters);

        long start = System.currentTimeMillis();

        int result = canBeTypedWords(text, brokenLetters);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
