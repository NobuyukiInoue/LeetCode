import java.util.*;

public class Solution {
    // 11ms
    String[] ones = {"", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"};
    String[] tens = {"", " Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"};
    String[] thousands = {"", " Thousand", " Million", " Billion"};

    public String numberToWords(int num) {
        if (num == 0) 
            return "Zero";
        return helper(num).substring(1);
    }

    public String helper(int n) {
        if (n < 20) 
            return ones[n];
        if (n < 100) 
            return tens[n / 10] + helper(n % 10);
        if (n < 1000) 
            return helper(n / 100) + " Hundred" + helper(n % 100);
        for (int i = 3; i >= 0; i--) {
            if (n >= Math.pow(1000, i)) {
                return helper((int)(n / Math.pow(1000, i))) + thousands[i] + helper((int)(n % Math.pow(1000, i)));
            }
        }
        return "";
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int num = Integer.parseInt(fld);
        System.out.println("num = " + num);

        long start = System.currentTimeMillis();

        String result = numberToWords(num);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
