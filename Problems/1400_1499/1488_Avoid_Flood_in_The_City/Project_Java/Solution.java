import java.util.*;

public class Solution {
    public int[] avoidFlood(int[] rains) {
        // 67ms
        Map<Integer, Integer> posMemo = new HashMap<>();
        TreeSet<Integer> slots = new TreeSet<>();
        int[] res = new int[rains.length];
        Arrays.fill(res, -1);

        for (int i = 0; i < rains.length; i++) {
            if (rains[i] == 0) {
                slots.add(i);
            } else {
                if (posMemo.containsKey(rains[i])){
                    Integer slot = slots.ceiling(posMemo.get(rains[i]));
                    if (slot == null)
                        return new int[0];
                    res[slot] = rains[i];
                    slots.remove(slot);
                }
                posMemo.put(rains[i], i);
            }
        }

        for (int s: slots)
            res[s] = 1;

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        int[] result = avoidFlood(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
