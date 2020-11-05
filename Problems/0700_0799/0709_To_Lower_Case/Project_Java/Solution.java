import java.util.*;

public class Solution {
    public String toLowerCase(String str) {
        if (str == null || str.length() <= 0) {
            return null;
        }
        
        char[] strCharArray = str.toCharArray();
        for (int i = 0; i < strCharArray.length; i++) {
            if (0x40 <= (int)strCharArray[i] && (int)strCharArray[i] <= 0x5a ) {
                strCharArray[i] += 0x20;
            }
        }

        return new String(strCharArray);
    }

    public void Main(String temp) {
        String str = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        System.out.println("str = " + str);

        long start = System.currentTimeMillis();

        String result = toLowerCase(str);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
