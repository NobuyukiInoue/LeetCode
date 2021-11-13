import java.util.*;

public class Solution {
    public String kthDistinct(String[] arr, int k) {
        // 4ms
        LinkedHashMap<String, Integer> map = new LinkedHashMap<>();
        for (String word : arr) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        int kth = 0;
		for (String key : map.keySet()) {
            if (map.get(key) == 1) {
                if (++kth == k) {
                    return key;
                }
            }
		}
        return "";
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String[] arr = flds[0].split(",");
        int k = Integer.parseInt(flds[1]);
        System.out.println("arr = " + ml.stringArrayToString(arr) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        String result = kthDistinct(arr, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
