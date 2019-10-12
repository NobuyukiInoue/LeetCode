import java.util.*;

public class Solution {
    public double myPow(double x, int n) {
        // 0ms
        double ans = 1;
        if (n < 0) {
            x = 1.0 / x;
            n = -n;
        }
        while (n != 0) {
            if (n % 2 == 1) {
                ans *= x;
            }
            x *= x;
            n >>>= 1;
        }
        return ans;
    }

    public String Int_array_to_String(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        double x = Double.parseDouble(flds[0]);
        int n = Integer.parseInt(flds[1]);
        System.out.println("x = " + Double.toString(x) + ", n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        double result = myPow(x, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Double.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
