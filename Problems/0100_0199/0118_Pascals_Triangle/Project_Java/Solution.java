import java.util.*;

public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for(int i = 1; i <= numRows; i++) {
            List<Integer> singleLine = new ArrayList<Integer>();
            for(int j = 1; j <= i; j++)
                singleLine.add(j == 1 || j == i ? 1 : result.get(i - 2).get(j - 2) + result.get(i - 2).get(j - 1));
            result.add(singleLine);
        }
        return result;
    }


    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int numRows = Integer.parseInt(flds);
        System.out.println("numRows = " + Integer.toString(numRows));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = generate(numRows);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
