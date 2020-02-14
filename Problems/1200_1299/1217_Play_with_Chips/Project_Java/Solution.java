import java.util.*;

public class Solution {
    public int minCostToMoveChips(int[] chips) {
        // 0ms
        int nOdd = 0, nEven = 0;
        for (int i : chips)
            if (i % 2 == 0)
                nEven++;
            else
                nOdd++;
        return Math.min(nEven, nOdd);
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
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] chips = mc.stringTointArray(flds);
        System.out.println("chips = [" + intArrayToString(chips) + "]");

        long start = System.currentTimeMillis();
        
        int result = minCostToMoveChips(chips);

        long end = System.currentTimeMillis();

        System.out.print("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
