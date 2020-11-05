import java.util.*;

public class Solution {
    public String removeDuplicates(String S) {
        int i = 0, n = S.length();
        char[] stack = new char[n];
        for (int j = 0; j < n; ++j)
            if (i > 0 && stack[i - 1] == S.charAt(j))
                --i;
            else
                stack[i++] = S.charAt(j);
        return new String(stack, 0, i);
    }

    public void Main(String temp) {
        String S = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("instructions = " + S);

        long start = System.currentTimeMillis();

        String result = removeDuplicates(S);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
