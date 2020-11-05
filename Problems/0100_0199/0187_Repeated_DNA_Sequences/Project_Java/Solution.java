import java.util.*;

public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        // 14ms
        Set seen = new HashSet(), repeated = new HashSet();
        for (int i = 0; i < s.length() - 9; i++) {
            String subStr = s.substring(i, i + 10);
            if (!seen.add(subStr)) {
                repeated.add(subStr);
            }
        }

        return new ArrayList(repeated);
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        List<String> result = findRepeatedDnaSequences(s);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
