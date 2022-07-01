import java.util.*;

public class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        // 54ms - 76ms
        Map<String, String> map = new HashMap<>();        
        for(List<String> list: knowledge) {
            map.put(list.get(0), list.get(1));
        }        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(') {
                int j = i;
                while (j < s.length() && s.charAt(j) != ')') {
                    j++;
                }
                sb.append(map.getOrDefault(s.substring(i + 1, j), "?"));
                i = j;
            } else sb.append(ch);
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim().split("\\],\\[\\[");

        Mylib ml = new Mylib();
        String s = flds[0].replace("[[", "");
        String[] flds1 = flds[1].replace("]]]", "").split("\\],\\[");
        List<List<String>> knowledge = ml.stringArrayToListListStringArray(flds1);
        System.out.println("s = \"" + s + "\", knowledge = " + ml.listListStringArrayToString(knowledge));

        long start = System.currentTimeMillis();

        String result = evaluate(s, knowledge);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
