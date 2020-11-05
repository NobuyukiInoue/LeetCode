import java.util.*;

public class Solution {
    public String removeKdigits(String num, int k) {
        // 2ms
        int remain = num.length() - k;
        char[] numArray = num.toCharArray();
        char[] res = new char[remain];
        int index = 0;
        for (int i = 0; i < numArray.length; i++) {
            while ((numArray.length - i > remain - index) && (index > 0 && numArray[i] < res[index - 1]))
                index--;
            if (index < remain)
                res[index++] = numArray[i];
        }

        index = -1;
        while (++index < remain) {
            if (res[index] != '0')
                break;
        }
        String s = new String(res).substring(index);

        if (s.length() == 0)
            return "0";
        return s;
    }

    public void Main(String temp) {
        String[] flds  = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String num = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("num = " + num + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        String result = removeKdigits(num, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
