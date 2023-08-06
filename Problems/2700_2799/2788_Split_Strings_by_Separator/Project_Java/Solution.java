import java.util.*;

public class Solution {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        // 5ms
        ArrayList<String> ans = new ArrayList<>();
        for (int i = 0; i < words.size(); i++) {
            StringBuilder sb = new StringBuilder();
            String word = words.get(i);
            for (char ch : word.toCharArray()) {
                if (ch != separator){
                    sb.append(ch);
                } else {
                    if (sb.length() > 0) {
                        ans.add(sb.toString());
                        sb.setLength(0);
                    }
                }
            }
            if (sb.length() > 0) {
                ans.add(sb.toString());
            }
        }
        return ans;
    }

    public List<String> splitWordsBySeparator2(List<String> words, char separator) {
        // 24ms - 25ms
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < words.size(); i++) {
            String[] flds = words.get(i).split("[" + separator + "]");
            for (String fld : flds) {
                if (fld.length() > 0) {
                    ans.add(fld);
                }
            }
        }
        return ans;
    }

    public List<String> splitWordsBySeparator_forEach(List<String> words, char separator) {
        // 27ms - 29ms
        List<String> ans = new ArrayList<>();
        words.forEach(word -> {
            String[] flds = word.split("[" + separator + "]");
            for (String fld : flds) {
                if (fld.length() > 0) {
                    ans.add(fld);
                }
            }
        });
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        String[] temp_words = flds[0].split(",");

        Mylib ml = new Mylib();
        List<String> words = Arrays.asList(temp_words);
       
        char separator = flds[1].charAt(0);

        System.out.println("words = " + ml.listStringArrayToString(words) + ", separator = '" + separator + "'");
        long start = System.currentTimeMillis();

        List<String> result = splitWordsBySeparator(words, separator);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
