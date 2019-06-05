import java.util.*;

public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for(int i = 0; i < rowIndex + 1; i++) {
            List<Integer> singleLine = new ArrayList<Integer>();
            for(int j = 0; j < i + 1; j++)
                singleLine.add(j == 0 || j == i ? 1 : result.get(i - 1).get(j - 1) + result.get(i - 1).get(j));
            result.add(singleLine);
        }
        return result.get(rowIndex);
    }

    public String List_array_to_String(List<Integer> list) {
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

        int rowIndex = Integer.parseInt(flds);
        System.out.println("rowIndex = " + Integer.toString(rowIndex));
 
        long start = System.currentTimeMillis();
        
        List<Integer> result = getRow(rowIndex);

        long end = System.currentTimeMillis();

        System.out.println("result = " + List_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
