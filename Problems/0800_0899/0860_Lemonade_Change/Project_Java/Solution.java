import java.util.*;

public class Solution {
    public boolean lemonadeChange(int[] bills) {
        int five = 0, ten = 0;
        for (int i : bills) {
            if (i == 5)
                five++;
            else if (i == 10) {
                five--; ten++;
            } else if (ten > 0) {
                ten--; five--;
            } else
                five -= 3;
            if (five < 0)
                return false;
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] bills = ml.stringToIntArray(flds);
        System.out.println("bills = " + ml.intArrayToString(bills));

        long start = System.currentTimeMillis();

        boolean result = lemonadeChange(bills);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
