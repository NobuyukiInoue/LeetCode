import java.util.*;

public class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        // 1ms
        int[] pat = findpat(pattern);
        List<String> res = new ArrayList<>();
        for (String word : words) {
            if (Arrays.equals(findpat(word), pat)) {
                res.add(word);
            }
        }
        return res;
    }

    private int[] findpat(String word) {
        HashMap<String, Integer> tbl = new HashMap<>();
        int m = 0;
        int[] pat = new int[word.length()];
        int i = 0;
        for (char ch : word.toCharArray()) {
            String chStr = String.valueOf(ch);
            if (! tbl.containsKey(chStr)) {  
                tbl.put(chStr, ++m);
            }
            pat[i++] = tbl.get(chStr);
        }
        return pat;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String[] words = flds[0].split(",");
        String pattern = flds[1];
        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words) + ", pattern = " + pattern);

        long start = System.currentTimeMillis();

        List<String> result = findAndReplacePattern(words, pattern);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
