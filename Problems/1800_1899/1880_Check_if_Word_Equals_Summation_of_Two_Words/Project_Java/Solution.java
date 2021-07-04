import java.util.*;

public class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        // 0ms
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        StringBuilder sb3 = new StringBuilder();
        int first = 0;
        int second = 0;
        int target = 0;

        for (int i = 0; i < firstWord.length(); i++) {
            sb1.append(firstWord.charAt(i) - 'a');
            first = Integer.parseInt(sb1.toString());
        }
        for (int i = 0; i < secondWord.length(); i++) {
            sb2.append(secondWord.charAt(i) - 'a');
            second = Integer.parseInt(sb2.toString());
        }
        for (int i = 0; i < targetWord.length(); i++) {
            sb3.append(targetWord.charAt(i) - 'a');
            target = Integer.parseInt(sb3.toString());
        }

        return  first + second == target;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String firstWord = flds[0];
        String secondWord = flds[1];
        String targetWord = flds[2];
        System.out.println("firstWord = " + firstWord + ", secondWord = " + secondWord + ", targetWord = " + targetWord);

        long start = System.currentTimeMillis();

        boolean result = isSumEqual(firstWord, secondWord, targetWord);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
