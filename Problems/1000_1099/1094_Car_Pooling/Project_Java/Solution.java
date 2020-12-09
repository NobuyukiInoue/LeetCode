import java.util.*;

public class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        // 5ms
        Map<Integer, Integer> tripMap = new TreeMap<>();
        for (int[] row : trips) {
            tripMap.put(row[1], tripMap.getOrDefault(row[1], 0) + row[0]);
            tripMap.put(row[2], tripMap.getOrDefault(row[2], 0) - row[0]);
        }
        int passengers = 0;
        for (int v : tripMap.values()) {
            passengers += v;
            if (passengers > capacity) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[[", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        int[][] trips = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        int capacity = Integer.parseInt(flds[1].replace("]", ""));
        System.out.println("trips = " + ml.intIntArrayToString(trips) + ", capacity = " + Integer.toString(capacity));

        long start = System.currentTimeMillis();

        boolean result = carPooling(trips, capacity);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
