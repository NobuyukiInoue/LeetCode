import java.util.*;

public class Solution {
    public boolean canReorderDoubled(int[] arr) {
        // 18ms
        HashMap<Integer, Integer> dic = new HashMap<>();

        for (int a : arr) {
            dic.put(a, dic.getOrDefault(a, 0) + 1);
        }

        int[] keys = new int[dic.size()];
        int i = 0;

        for (Integer key : dic.keySet()) {
            keys[i++] = key;
        }
        Arrays.sort(keys);

        for (int k : keys) {
            int get_k = dic.get(k);
            if (get_k != 0 && dic.containsKey(2*k)) {
                int get_2k = dic.get(2*k);
                if (get_k > get_2k) {
                    dic.put(k, get_k - get_2k);
                    dic.put(k*2, 0);
                } else {
                    dic.put(2*k, get_2k - get_k);
                    dic.put(k, 0);
                }
            }
        }

        for (int v : dic.values()) {
            if (v != 0) {
                return false;
            }
        }
        return true;
    }

    public boolean canReorderDoubled2(int[] arr) {
        // 25ms
        HashMap<Integer, Integer> dic = new HashMap<>();
        for (int a : arr) {
            dic.put(a, dic.getOrDefault(a, 0) + 1);
        }

        int[] keys = new int[dic.size()];
        int i = 0;
        for (Integer key : dic.keySet()) {
            keys[i++] = key;
        }
        Arrays.sort(keys);

        for (int k : keys) {
            if (dic.get(k) != 0 && dic.containsKey(2*k)) {
                if (dic.get(k) > dic.get(k*2)) {
                    dic.put(k, dic.get(k) - dic.get(k*2));
                    dic.put(k*2, 0);
                } else {
                    dic.put(2*k, dic.get(2*k) - dic.get(k));
                    dic.put(k, 0);
                }
            }
        }

        for (int v : dic.values()) {
            if (v != 0) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        boolean result = canReorderDoubled(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
