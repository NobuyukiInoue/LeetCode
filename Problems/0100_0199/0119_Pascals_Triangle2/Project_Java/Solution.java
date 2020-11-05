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

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int rowIndex = Integer.parseInt(flds);
        System.out.println("rowIndex = " + Integer.toString(rowIndex));
 
        long start = System.currentTimeMillis();
        
        List<Integer> result = getRow(rowIndex);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
