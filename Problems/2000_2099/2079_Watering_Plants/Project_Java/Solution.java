import java.util.*;

public class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        // 0ms
        int ans = 0, water = capacity;
        for (int i = 0; i < plants.length; i++) {
            if (plants[i] <= water) {
                water -= plants[i];
                ans++;
            } else {
                water = capacity - plants[i];
                ans += 2*i + 1;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] plants = ml.stringToIntArray(flds[0]);
        int capacity = Integer.parseInt(flds[1]);
        System.out.println("plants = " + ml.intArrayToString(plants) + ", capacity = " + capacity);
 
        long start = System.currentTimeMillis();

        int result = wateringPlants(plants, capacity);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
