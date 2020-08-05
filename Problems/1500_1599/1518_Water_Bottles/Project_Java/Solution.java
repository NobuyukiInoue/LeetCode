import java.util.*;

public class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        // 0ms
        int exchangedBottles = 0;
        while (numBottles >= numExchange) {
            int divBottles = numBottles / numExchange;
            exchangedBottles += divBottles*numExchange;
            numBottles = numBottles % numExchange + divBottles;
        }
        return exchangedBottles + numBottles;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        int numBottles  = Integer.parseInt(flds[0]);
        int numExchange = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();

        int result = numWaterBottles(numBottles, numExchange);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
