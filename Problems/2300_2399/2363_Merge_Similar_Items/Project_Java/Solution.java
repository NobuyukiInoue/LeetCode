import java.util.*;

public class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {
        // 13ms - 21ms
        HashMap<Integer, Integer> records = new HashMap<>();
        for (int[] item : items1) {
            records.put(item[0], records.getOrDefault(item[0], 0) + item[1]);
        }
        for (int[] item : items2) {
            records.put(item[0], records.getOrDefault(item[0], 0) + item[1]);
        }

        List<List<Integer>> ans = new ArrayList<>();
        for(int key : records.keySet()){
            List<Integer> curr = new ArrayList<>();
            curr.add(key);
            curr.add(records.get(key));
            ans.add(curr);
        }

        Collections.sort(ans, (o1, o2) -> (o1.get(0) - o2.get(0)));
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(", ", ",").replace("[[[", "").replace("]]]", "").trim().split("\\]\\],\\[\\[");

        Mylib ml = new Mylib();
        int[][] items1 = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        System.out.println("items1 = " + ml.matrixToString(items1));
        int[][] items2 = ml.stringToIntIntArray(flds[1].split("\\],\\["));
        System.out.println("items2 = " + ml.matrixToString(items2));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = mergeSimilarItems(items1, items2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
