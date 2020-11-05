import java.util.*;

public class Solution {
    public String destCity(List<List<String>> paths) {
        // 2ms
        Set<String> set= new HashSet<>();

        for (List<String> l: paths)
            set.add(l.get(1));

        for (List<String> l: paths)
            set.remove(l.get(0));

        return set.iterator().next();
    }

    public String destCity2(List<List<String>> paths) {
        // 1ms
        HashSet<String> set = new HashSet<>();
        String result = "";

        for (int i = 0; i < paths.size(); i++) {
            set.add(paths.get(i).get(0));
        }

        for (int i = 0; i < paths.size(); i++) {
            if (!set.contains(paths.get(i).get(1))) {
                result = paths.get(i).get(1);
                break;
            }
        }

        return result;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] data = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<String>> paths = ml.stringArrayToListListStringArray(data);
        System.out.println("paths = " + ml.listListStringArrayToString(paths));

        long start = System.currentTimeMillis();

        String result = destCity(paths);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
