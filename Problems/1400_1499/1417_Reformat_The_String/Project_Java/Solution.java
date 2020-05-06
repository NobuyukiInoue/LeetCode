import java.util.*;

public class Solution {
    public String reformat(String s) {
        // 1ms
        if (s.length() == 1)
            return s;
    
        char[] digits = new char[s.length()];
        char[] letters = new char[s.length()];

        int i = -1;
        int j = -1;

        for (char c : s.toCharArray())
            if (c >= '0' && c <= '9')
                digits[++i] = c;
            else
                letters[++j] = c;

        int lettersCount = j + 1;
        int digitCount = i + 1;

        if (lettersCount == 0 || digitCount == 0 || Math.abs(lettersCount - digitCount) > 1)
            return "";

        char[] result = new char[s.length()];
        if (lettersCount > digitCount) {
            int k = 0;
            for (int x = 0;x < lettersCount; x++, k += 2)
                result[k] = letters[x];
            k = 1;
            for (int y = 0; y < digitCount; y++, k += 2)
                result[k] = digits[y];
        } else {
            int k = 0;
            for (int y = 0; y < digitCount; y++, k += 2)
                result[k] = digits[y];
            k = 1;
            for (int x = 0; x < lettersCount; x++, k += 2)
                result[k] = letters[x];
        }
        return new String(result);
    }

    public String reformat2(String s) {
        // 5ms
        StringBuilder nums = new StringBuilder();
        StringBuilder letters = new StringBuilder();

        for (int i = 0; i < s.length(); i++)
            if (Character.isDigit(s.charAt(i)))
                nums.append(s.charAt(i));
            else
                letters.append(s.charAt(i));

        if (Math.abs(nums.length() - letters.length()) > 1)
            return "";

        StringBuilder res = new StringBuilder();
        int i;
        if (nums.length() > letters.length()) {
            for (i = 0; i < letters.length(); i++)
                res.append(String.valueOf(nums.charAt(i)) + String.valueOf(letters.charAt(i)));
            res.append(nums.charAt(i));

        } else if (letters.length() > nums.length()) {
            for (i = 0; i < nums.length(); i++)
                res.append(String.valueOf(letters.charAt(i)) + String.valueOf(nums.charAt(i)));
            res.append(letters.charAt(i));

        } else {
            for (i = 0; i < nums.length(); i++) {
                res.append(String.valueOf(letters.charAt(i)) + String.valueOf(nums.charAt(i)));
            }
        }

        return res.toString();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        String result = reformat(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
