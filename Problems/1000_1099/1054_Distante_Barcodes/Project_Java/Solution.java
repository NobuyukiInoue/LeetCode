import java.util.*;
import java.util.Collections;
import java.util.Map;
import java.util.Map.Entry;

public class Solution {
    public int[] rearrangeBarcodes(int[] barcodes) {
        // 30ms
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : barcodes) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }

        List<Entry<Integer, Integer>> list_entries = new ArrayList<Entry<Integer, Integer>>(map.entrySet());
        Collections.sort(list_entries, new Comparator<Entry<Integer, Integer>>() {
            public int compare(Entry<Integer, Integer> obj1, Entry<Integer, Integer> obj2)
            {
                // sort reverse
                return obj2.getValue().compareTo(obj1.getValue());
            }
        });

        int[] res = new int[barcodes.length];
        int i = 0;
        for(Entry<Integer, Integer> entry : list_entries) {
            for (int count = 0; count < entry.getValue(); count++) {
                res[i] = entry.getKey();
                i += 2;
                if (i >= barcodes.length) {
                    i = 1;
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] barcodes = ml.stringToIntArray(flds);
        System.out.println("barcodes = " + ml.intArrayToString(barcodes));

        long start = System.currentTimeMillis();

        int[] result = rearrangeBarcodes(barcodes);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
