import java.util.*;

public class Solution {
    public int subarrayBitwiseORs(int[] arr) {
        // 146ms
        int[] size = {1};
        HashMap<Integer,Integer> map = new HashMap<>();

        func(arr, size, arr.length);

        for (int i = 0;i < size[0]; i++) {
            map.put(arr[i],1);
        }

        while (size[0] > 1) {
            hepler(arr, size, map);
        }

        return map.keySet().size();
    }

    public void func(int[] arr, int[] size, int length){
        for (int i = 1; i < length; i++) {
            if (arr[i] != arr[size[0] - 1]) {
                arr[size[0]++] = arr[i];
            }
        }
    }

    public void hepler(int[] arr, int[] size, HashMap map){
        for (int i = 0; i < size[0] - 1; i++) {
            arr[i] |= arr[i + 1];
            map.put(arr[i], 1);
        }
        int tmp = size[0] - 1;
        size[0] = 1;
        func(arr, size, tmp);
    }

    public int subarrayBitwiseORs_HashSet(int[] arr) {
        // 367ms
        Set<Integer> res = new HashSet<>(), cur = new HashSet<>(), cur2;
        for (Integer i: arr) {
            cur2 = new HashSet<>();
            cur2.add(i);
            for (Integer j: cur) cur2.add(i|j);
            res.addAll(cur = cur2);
        }
        return res.size();
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        int result = subarrayBitwiseORs(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
