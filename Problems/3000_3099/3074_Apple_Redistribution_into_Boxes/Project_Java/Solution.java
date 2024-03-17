import java.util.*;

public class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        // 1ms - 2ms
        Arrays.sort(capacity);
//      int total =  Arrays.stream(apple).sum();    // 4ms - 5ms
        int total = 0;
        for (int app : apple) {
            total += app;
        }
        int t_cap = 0;
        for (int i = 0; i < capacity.length; i++) {
            if (t_cap >= total) {
                return i;
            }
            t_cap += capacity[capacity.length - 1 - i];
        }
        return capacity.length;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] apple = ml.stringToIntArray(flds[0]);
        int[] capacity = ml.stringToIntArray(flds[1]);
        System.out.println("apple = " + ml.intArrayToString(apple) + ", capacity = " + ml.intArrayToString(capacity));

        long start = System.currentTimeMillis();

        int result = minimumBoxes(apple, capacity);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
