import java.util.*;

public class Solution {
    public String multiply(String num1, String num2) {
        int m = num1.length(), n = num2.length();
        int[] pos = new int[m + n];

        for(int i = m - 1; i >= 0; i--) {
            for(int j = n - 1; j >= 0; j--) {
                int mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0'); 
                int p1 = i + j, p2 = i + j + 1;
                int sum = mul + pos[p2];

                pos[p1] += sum / 10;
                pos[p2] = (sum) % 10;
            }
        }  

        StringBuilder sb = new StringBuilder();
        for(int p : pos)
            if(!(sb.length() == 0 && p == 0))
                sb.append(p);

        if (sb.length() == 0)
            return "0";
        return sb.toString();
    }

    public String multiply_bad(String num1, String num2) {
        int[] v_num1 = new int[num1.length()];
        int[] v_num2 = new int[num2.length()];

        for (int i = 0; i < num1.length(); ++i) {
            v_num1[i] = num1.charAt(i) - '0';
        }
        for (int i = 0; i < num2.length(); ++i) {
            v_num2[i] = num2.charAt(i) - '0';
        }

        long val1 = 0;
        for (int n : v_num1) {
            val1 *= 10;
            val1 += n;
        }

        long result = 0;
        for (int m : v_num2) {
            result *= 10;
            result += val1 * m;
        } 

        return Long.toString(result);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        String num1 = flds[0];
        String num2 = flds[1];

        long start = System.currentTimeMillis();

        String result = multiply(num1, num2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
