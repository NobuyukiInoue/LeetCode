import java.util.*;
import java.util.AbstractMap;

public class Solution {
    private static Map<Integer, String> conversionMap = new LinkedHashMap<Integer, String>(){{
        put(1000,"M"); put(900, "CM"); put(500,"D"); put(400,"CD"); put(100, "C");
        put(90, "XC");put(50,"L"); put(40,"XL");put(10,"X");put(9,"IX");
        put(5, "V"); put(4,"IV");put(1,  "I");
    }};

    public static String intToRoman(int num) {
        // 12ms
        if(num <= 0)
            return "";
        Map.Entry<Integer,String> entry = getConversion(num);
        return entry.getValue() + intToRoman(num - entry.getKey());
    }

    private static Map.Entry<Integer,String> getConversion(int val) {
        for (Map.Entry<Integer,String> i : conversionMap.entrySet()) {
            if (i.getKey() <= val)
                return i;
        }
        return new AbstractMap.SimpleEntry<>(0, "");
    }

/*
    public String intToRoman(int num) {
    	// 5ms
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1};
        String[] strs = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < values.length; i++) {
            while (num >= values[i]) {
                num -= values[i];
                sb.append(strs[i]);
            }
        }
        return sb.toString();
    }
*/
    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        int num = Integer.parseInt(fld);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        String result = intToRoman(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
