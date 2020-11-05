import java.util.*;

public class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        Map<String, Integer> map = new HashMap<>();
        List<String> res = new LinkedList<>();
        int minSum = Integer.MAX_VALUE;

        for (int i=0;i<list1.length;i++)
            map.put(list1[i], i);

        for (int i=0;i<list2.length;i++) {
            Integer j = map.get(list2[i]);
            if (j != null && i + j <= minSum) {
                if (i + j < minSum) { res.clear(); minSum = i+j; }
                res.add(list2[i]);
            }
        }

        return res.toArray(new String[res.size()]);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String[] list1 = flds[0].split(",");
        String[] list2 = flds[1].split(",");

        Mylib ml = new Mylib();
        System.out.println("list1 = " + ml.stringArrayToString(list1));
        System.out.println("list2 = " + ml.stringArrayToString(list2));

        long start = System.currentTimeMillis();

        String[] result = findRestaurant(list1, list2);

        long end = System.currentTimeMillis();

        System.out.println("result = " +  ml.stringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
