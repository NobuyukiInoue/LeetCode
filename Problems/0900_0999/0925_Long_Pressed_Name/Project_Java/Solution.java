import java.util.*;

public class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int i = 0, m = name.length(), n = typed.length();
        for (int j = 0; j < n; ++j)
            if (i < m && name.charAt(i) == typed.charAt(j))
                ++i;
            else if (j == 0 || typed.charAt(j) != typed.charAt(j - 1))
                return false;
        return i == m;
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
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String name = flds[0];
        String typed = flds[1];

        System.out.println("name = " + name + ", typed = " + typed);

        long start = System.currentTimeMillis();
        
        Boolean result = isLongPressedName(name, typed);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
