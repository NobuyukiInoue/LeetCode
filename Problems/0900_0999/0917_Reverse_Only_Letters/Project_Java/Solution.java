import java.util.*;

public class Solution {
    public String reverseOnlyLetters(String S) {
        StringBuilder sb = new StringBuilder(S);

        for (int i = 0, j = S.length() - 1; i < j; ++i, --j) {
            while (i < j && !Character.isLetter(sb.charAt(i)))
                ++i;
            while (i < j && !Character.isLetter(sb.charAt(j)))
                --j;
            sb.setCharAt(i, S.charAt(j));
            sb.setCharAt(j, S.charAt(i));
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String S = temp.replace("\"", "").replace("[", "").replace("]", "").trim();

        System.out.println("S = " + S);

        long start = System.currentTimeMillis();

        String result = reverseOnlyLetters(S);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
