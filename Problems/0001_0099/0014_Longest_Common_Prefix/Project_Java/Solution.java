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

    public void Main(String temp) {
        String[] strs  = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("strs = " + ml.stringArrayToString(strs));

        long start = System.currentTimeMillis();

        String result = longestCommonPrefix(strs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
