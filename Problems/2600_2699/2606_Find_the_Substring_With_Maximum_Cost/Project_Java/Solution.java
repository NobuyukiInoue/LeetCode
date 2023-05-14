import java.util.*;

public class Solution {
    public int maximumCostSubstring(String s, String chars, int[] vals) {
        // 7ms
        int[] char_dict = new int[26];
        for (int i = 0; i < 26; i++) {
            char_dict[i] = i + 1;
        }
        for (int i = 0; i < chars.length(); i++) {
            char_dict[chars.charAt(i) - 'a'] = vals[i];
        }
        int max_cost = 0, curr_cost = 0;
        for (char ch : s.toCharArray()) {
            curr_cost += char_dict[ch - 'a'];
            if (curr_cost < 0) {
                curr_cost = 0;
            }
            if (curr_cost > max_cost) {
                max_cost = curr_cost;
            }
        }
        return max_cost;
    }

    public int maximumCostSubstring2(String s, String chars, int[] vals) {
        // 24ms
        HashMap<Character, Integer> char_dict = new HashMap<>();
        for (int i = 0; i < chars.length(); i++) {
            char_dict.put(chars.charAt(i), vals[i]);
        }
        int max_cost = 0, curr_cost = 0;
        for (char ch : s.toCharArray()) {
            if (!char_dict.containsKey(ch)) {
                curr_cost += ch - 'a' + 1;
            } else {
                curr_cost += char_dict.get(ch);
            }
            if (curr_cost < 0) {
                curr_cost = 0;
            }
            if (curr_cost > max_cost) {
                max_cost = curr_cost;
            }
        }
        return max_cost;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        String s = flds[0];
        String chars = flds[1];
        int[] vals = ml.stringToIntArray(flds[2]);

        System.out.println("s = \"" + s + "\", chars = \"" + chars + "\", vals = " + ml.intArrayToString(vals));
        long start = System.currentTimeMillis();

        int result = maximumCostSubstring(s, chars, vals);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
