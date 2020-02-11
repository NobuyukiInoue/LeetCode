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

    private String stringArrayToString(String[] flds) {
        if (flds.length <= 0)
            return "";
        StringBuilder sb = new StringBuilder();
        sb.append("[" + flds[0]);
        for (int i = 1; i < flds.length; i++)
            sb.append(", " + flds[i]);

        return sb.append("]").toString();
    }

    private String listlistArrayToString(List<List<String>> flds) {
        if (flds.size() <= 0)
            return "";
        StringBuilder sb = new StringBuilder();
        sb.append("[" + listArrayToString(flds.get(0)));
        for (int i = 1; i < flds.size(); i++)
            sb.append(", " + listArrayToString(flds.get(i)));

        return sb.append("]").toString();
    }

    private String listArrayToString(List<String> flds) {
        if (flds.size() <= 0)
            return "";
        StringBuilder sb = new StringBuilder();
        sb.append("[" + flds.get(0));
        for (int i = 1; i < flds.size(); i++)
            sb.append(", " + flds.get(i));

        return sb.append("]").toString();
    }

    public void Main(String temp) {
        String[] strs = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").trim().split(",");
        System.out.println("strs = " + stringArrayToString(strs));

        long start = System.currentTimeMillis();
        
        List<List<String>> result = groupAnagrams(strs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listlistArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
