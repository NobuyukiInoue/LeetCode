import java.util.*;

public class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        // 7ms
        Arrays.sort(boxTypes, (a, b) -> Integer.compare(b[1], a[1]));
        int cnt_unit = 0, cnt_box = 0;
        for (int[] target :boxTypes) {
            if (cnt_box + target[0] <= truckSize) {
                cnt_unit += target[0]*target[1];
                cnt_box += target[0];
            } else {
                int i;
                if (target[0] <= truckSize - cnt_box) {
                    i = target[0];
                } else {
                    i = truckSize - cnt_box;
                }
                cnt_unit += target[1]*i;
                cnt_box += i;
            }
            if (cnt_box >= truckSize) {
                break;
            }
        }
        return cnt_unit;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[[", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        int[][] boxTypes   = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        System.out.println("boxTypes  = " + ml.intIntArrayToString(boxTypes));
        int truckSize = Integer.parseInt(flds[1].replace("]", ""));
        System.out.println("truckSize = " + Integer.toString(truckSize));

        long start = System.currentTimeMillis();

        int result = maximumUnits(boxTypes, truckSize);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
