import java.util.*;

public class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        // 0ms
        String[] words = text.split(" ");
        List<String> ans = new ArrayList<>();
        for (int i = 2; i < words.length; i++) {
            if (first.equals(words[i - 2]) && second.equals(words[i - 1]))
                ans.add(words[i]);
        }
        return ans.toArray(new String[0]);
    }

    private String stringArrayToString(String[] flds) {
        if (flds.length <= 0)
            return "[]";
        StringBuilder sb = new StringBuilder("[\"" + flds[0] + "\"");
        for (int i = 1; i < flds.length; i++)
            sb.append(", \"" + flds[i] + "\"");
        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        String text = flds[0];
        String first = flds[1];
        String second = flds[2];

        System.out.println("text = " + text + ", first = " + first + ", second = " + second);

        long start = System.currentTimeMillis();
        
        String[] result = findOcurrences(text, first, second);

        long end = System.currentTimeMillis();

        System.out.println("result = " + stringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
