import java.util.*;

public class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        // 3ms
        int res = 0, col = 0;

        switch (ruleKey) {
        case "type":
            col = 0;
            break;
        case "color":
            col = 1;
            break;
        case "name":
            col = 2;
            break;
        }

        for (List<String> item : items) {
            if (ruleValue.equals(item.get(col))) {
                res++;
            }
        }

        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[[", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        List<List<String>> items = ml.stringArrayToListListStringArray(flds[0].split("\\],\\["));
        System.out.println("items = " + ml.listListStringArrayToString(items));

        String[] flds1 = flds[1].replace("]]", "").split("\\],\\[");
        String ruleKey = flds1[0];
        String ruleValue = flds1[1];
        System.out.println("ruleKey = " + ruleKey + ", ruleValue = " + ruleValue);

        long start = System.currentTimeMillis();

        int result = countMatches(items, ruleKey, ruleValue);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
