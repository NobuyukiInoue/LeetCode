import java.util.*;

public class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        // 0ms
        int i = 0;
        while (i < arr.length - 2) {
            if (arr[i] % 2 == 0) {
                i++;
                continue;
            }
            i++;
            if (arr[i] % 2 == 0)
                continue;
            i++;
            if (arr[i] % 2 == 0)
                continue;
            return true;
        }
        return false;
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
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringTointArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();
        
        boolean result = threeConsecutiveOdds(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
