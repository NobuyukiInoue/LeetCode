import java.util.*;

public class Solution {
    public int compress(char[] chars) {
        // 1ms
        if (chars == null || chars.length == 0)
            return 0;
        int index = 0, n = chars.length, i = 0;
        while (i < n) {
            char ch = chars[i];
            int j = i;
            while (j < n && chars[i] == chars[j]) {
                j++;
            }
            int freq = j - i;
            chars[index++] = ch;
            if (freq == 1) {

            } else if (freq < 10) {
                chars[index++] = (char)(freq + '0');
            } else {
                String strFreq = String.valueOf(freq);
                for (char chFreq : strFreq.toCharArray())
                    chars[index++] = chFreq;
            }
            i = j;
        }
        return index;
    }

    public String output_str_array(String[] words) {
        String result = "[";

        for (int i = 0; i < words.length; i++) {
            if (i == 0) {
                result += "\"" + words[i] + "\"";
            } else {
                result += ",\"" + words[i] + "\"";
            }
        }

        return result + "]";
    }

    public void Main(String temp) {
        String flds  = temp.replace("[", "").replace("]", "").replace(", ", ",").replace("\"", "").replace(",", "").trim();
        char chars[] = flds.toCharArray();

        System.out.println("chars = " + String.valueOf(chars));

        long start = System.currentTimeMillis();
        
        int result = compress(chars);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result) + ", chars = " + String.valueOf(chars));
        System.out.println((end - start)  + "ms\n");
    }
}
