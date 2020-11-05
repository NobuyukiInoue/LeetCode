import java.util.*;

public class Solution {
    public int findLucky(int[] arr) {
        // 3ms
        Map<Integer, Integer> freq = new HashMap<>();
        for (int a : arr) {
            freq.put(a, 1 + freq.getOrDefault(a, 0));
        }
        int ans = -1;
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            if (e.getKey() == e.getValue()) {
                ans = Math.max(ans, e.getKey());
            }
        }
        return ans;
    }

    public int findLucky2(int[] arr) {
        // 1ms
        int[] temp = new int[501];

        for(int i:arr)
            temp[i]++;

        for(int i = temp.length - 1; i >= 1; i--) {
            if(temp[i]==i)
                return i;
        }
        return -1;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();
        
        int result = findLucky(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
