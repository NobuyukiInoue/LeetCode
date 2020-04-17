import java.util.*;

public class Solution {
    public List<String> stringMatching(String[] words) {
        // 3ms
        Set<String> set = new HashSet<>();
        int n = words.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j == i)
                    continue;
                if (words[j].contains(words[i])) {
                    set.add(words[i]);
                    break;
                }
            }
        }
        return new ArrayList<>(set);
    }

    public String strArrayToString(String[] words) {
        StringBuilder result = new StringBuilder();
        result.append("[");

        for (int i = 0; i < words.length; i++) {
            if (i == 0) {
                result.append("\"" + words[i] + "\"");
            } else {
                result.append(",\"" + words[i] + "\"");
            }
        }

        return result.append("]").toString();
    }

    private String listArrayToString(List<String> arr) {
        if (arr.size() <= 0)
            return "";
        StringBuffer sb = new StringBuffer("[" + arr.get(0));
        for (int i = 1; i < arr.size(); i++) {
            sb.append(", " + arr.get(i));
        }
        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        System.out.println("words = " + strArrayToString(words));

        long start = System.currentTimeMillis();
        
        List<String> result = stringMatching(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
