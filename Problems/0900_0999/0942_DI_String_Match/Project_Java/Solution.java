import java.util.*;

public class Solution {
    public int[] diStringMatch(String S) {
        int n = S.length(), left = 0, right = n;
        int[] res = new int[n + 1];
        for (int i = 0; i < n; ++i)
            res[i] = S.charAt(i) == 'I' ? left++ : right--;
        res[n] = left;
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
        String S = temp.replace("\"", "").replace("[", "").replace("]", "").trim();
        System.out.println("S = " + S);

        long start = System.currentTimeMillis();
        
        int[] result = diStringMatch(S);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
