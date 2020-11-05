import java.util.*;

public class Solution {
    public List<String> alertNames(String[] keyName, String[] keyTime) {
        // 69ms
        Map<String, TreeSet<Integer>> nameToTime = new HashMap<>();
        for (int i = 0; i < keyName.length; i++) {
            int timeMinutes = Integer.parseInt(keyTime[i].substring(0, 2))*60 + Integer.parseInt(keyTime[i].substring(3));
            nameToTime.computeIfAbsent(keyName[i], s -> new TreeSet<>()).add(timeMinutes);
        }

        TreeSet<String> names = new TreeSet<>();
        for (Map.Entry<String, TreeSet<Integer>> e : nameToTime.entrySet()) {
            List<Integer> list = new ArrayList<>(e.getValue());
            for (int i = 2; i < list.size(); i++) {
                if (list.get(i) - list.get(i - 2) <= 60) {
                    names.add(e.getKey());
                    break;
                }
            }
        }

        return new ArrayList<>(names);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").trim().split("\\],\\[");
        String[] keyName = flds[0].replace("[[", "").split(",");
        String[] keyTime = flds[1].replace("]]", "").split(",");

        Mylib ml = new Mylib();
        System.out.println("keyName = " + ml.stringArrayToString(keyName));
        System.out.println("keyTime = " + ml.stringArrayToString(keyTime));

        long start = System.currentTimeMillis();

        List<String> result = alertNames(keyName, keyTime);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
