import java.util.*;

public class Solution {
    public int differenceOfSums(int n, int m) {
        // 0ms
        return (1 + n) * n / 2 - (1 + n / m) * (n / m) * m;
    }

    public int differenceOfSums2(int n, int m) {
        // 1ms
        int num1 = 0, num2 = 0;
        for (int i = 1; i < n + 1; i++) {
            if (i % m != 0) {
                num1 += i;
            } else {
                num2 += i;
            }
        }
        return num1 - num2;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int m = Integer.parseInt(flds[1]);
        System.out.println("n = " + n + ", m = " + m);
 
        long start = System.currentTimeMillis();

        int result = differenceOfSums(n, m);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
