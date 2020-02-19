import java.util.Locale;

public class Solution {
    public boolean canMeasureWater(int x, int y, int z) {
        // 0ms
        if (x + y < z)
            return false;
        if( x == z || y == z || x + y == z )
            return true;
        return z%GCD(x, y) == 0;
    }
    
    public int GCD(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a%b;
            a = temp;
        }
        return a;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        int x = Integer.parseInt(flds[0]);
        int y = Integer.parseInt(flds[1]);
        int z = Integer.parseInt(flds[2]);
        System.out.println(String.format(Locale.JAPAN, "x = %d, y = %d, z = %d", x, y, z));

        long start = System.currentTimeMillis();

        boolean result = canMeasureWater(x, y, z);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
