import java.util.*;

public class Solution {
    public int[] minOperations(String boxes) {
        // 4ms - 5ms
        int total = 0, move_count = 0;
        int[] res = new int[boxes.length()];
        for (int i = 0; i < boxes.length(); i++) {
            res[i] = move_count;
            if (boxes.charAt(i) == '1') {
                total++;
            }
            move_count += total;
        }
        total = move_count = 0;
        for (int i = boxes.length() - 1; i >= 0; i--) {
            res[i] += move_count;
            if (boxes.charAt(i) == '1') {
                total++;
            }
            move_count += total;
        }
        return res;
    }

    public void Main(String temp) {
        String boxes = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("boxes = " + boxes);

        long start = System.currentTimeMillis();

        int[] result = minOperations(boxes);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
