import java.util.*;

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        // 0ms
        String res = strs.length == 0 ? "" : strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(res) != 0) {
                res=res.substring(0, res.length() - 1);
            }
        }
        return res;
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
        String[] strs  = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");
        System.out.println("strs = " + output_str_array(strs));

        long start = System.currentTimeMillis();
        
        String result = longestCommonPrefix(strs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
