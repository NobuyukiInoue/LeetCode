import java.util.*;

public class Solution {
    public int subtractProductAndSum(int n) {
        // 0ms
        int prod = 1;
        int sum = 0;
        while(n > 0){
            prod *= n %10;
            sum += n % 10;
            n /= 10;
        }
        return prod - sum;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = subtractProductAndSum(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
