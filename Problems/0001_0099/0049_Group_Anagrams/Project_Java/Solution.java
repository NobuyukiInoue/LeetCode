import java.util.*;

public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // 6ms
        if (strs == null || strs.length == 0)
            return new ArrayList<List<String>>();

        Map<String, List<String>> map = new HashMap<String, List<String>>();

        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String keyStr = String.valueOf(ca);
            if (!map.containsKey(keyStr))
                map.put(keyStr, new ArrayList<String>());
            map.get(keyStr).add(s);
        }

        return new ArrayList<List<String>>(map.values());
    }

    public void Main(String temp) {
        String[] strs = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("strs = " + ml.stringArrayToString(strs));

        long start = System.currentTimeMillis();

        List<List<String>> result = groupAnagrams(strs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
