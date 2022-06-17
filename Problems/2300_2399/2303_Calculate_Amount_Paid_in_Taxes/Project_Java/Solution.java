import java.util.*;

public class Solution {
    public double calculateTax(int[][] brackets, int income) {
        // 1ms
        double tax = 0.0;
        int prev = 0;
        for (int[] bracket : brackets) {
            if (income >= bracket[0]) {
                tax += (bracket[0] - prev)*bracket[1]/100.0;
                prev = bracket[0];
            } else {
                tax += (income - prev)*bracket[1]/100.0;
                return tax;
            }
        }
        return tax;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").split("\\]\\],\\[");
        String[] flds0 = flds[0].split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] brackets = ml.stringToIntIntArray(flds0);
        int income = Integer.parseInt(flds[1].replace("]",""));
        System.out.println("brackets = " + ml.intIntArrayToString(brackets) + ", income = " + Integer.toString(income));

        long start = System.currentTimeMillis();

        double result = calculateTax(brackets, income);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Double.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
