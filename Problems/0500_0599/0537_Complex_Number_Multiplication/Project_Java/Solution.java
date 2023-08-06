import java.util.*;

public class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        // 4ms
        String[] flds1 = num1.split("\\+");
        String[] flds2 = num2.split("\\+");
        int n1r = Integer.parseInt(flds1[0]);
        int n1i = Integer.parseInt(flds1[1].substring(0, flds1[1].length() - 1));
        int n2r = Integer.parseInt(flds2[0]);
        int n2i = Integer.parseInt(flds2[1].substring(0, flds2[1].length() - 1));
        int re = n1r*n2r - n1i*n2i;
        int im = n1r*n2i + n1i*n2r;
        return re + "+" + im + "i";
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");
        String num1 = flds[0];
        String num2 = flds[1];
        System.out.println("num1 = \"" + num1 + "\", num2 = \"" + num2 + "\"");

        long start = System.currentTimeMillis();

        String result = complexNumberMultiply(num1, num2);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
