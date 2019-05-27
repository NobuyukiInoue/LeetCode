import java.util.*;

public class Solution {
    public int numSpecialEquivGroups(String[] A) {
        HashSet<String> set = new HashSet<>();
        for (String s : A) {
            char[] chars = s.toCharArray();
            for (int i = 0; i < chars.length; i += 2)
                chars[i] += 26;
            Arrays.sort(chars);
            set.add(String.valueOf(chars));
        }
        return set.size();
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
        String[] A = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        System.out.println("A = " + output_str_array(A));

        long start = System.currentTimeMillis();
        
        int result = numSpecialEquivGroups(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
