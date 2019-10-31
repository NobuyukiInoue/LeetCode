import java.util.*;

public class Solution {
    public int numDecodings(String s) {
        // 2ms
        if (s.isEmpty() || s.charAt(0) == '0')
            return 0;

		int len_s = s.length();
        int[] results = new int[len_s + 1];
		results[0] = results[1] = 1;

		for (int i = 2; i <= len_s; i++) {
            int first  = Integer.parseInt(s.substring(i - 1, i));
            int second = Integer.parseInt(s.substring(i - 2, i));

            if (first >= 1 && first <= 9)
                results[i] += results[i - 1];
            if (second >= 10 && second <= 26)
                results[i] += results[i - 2];
        }
        return results[len_s];
    }

    public String intArrayToString(int[] data) {
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

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        int result = numDecodings(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
