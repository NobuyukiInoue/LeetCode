import java.util.*;

public class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();

        Arrays.sort(arr);
        Integer var_min = 10^7;
        int var_sub = 0;

        for (int i = 0; i < arr.length - 1; ++i) {
            var_sub = arr[i + 1] - arr[i];
            if (var_sub < var_min) {
                var_min = var_sub;
            }
        }

        for (int i = 0; i < arr.length - 1; ++i) {
            var_sub = arr[i + 1] - arr[i];
            if (var_sub == var_min) {
                List<Integer> temp = new ArrayList<Integer>();
                temp.add(arr[i]);
                temp.add(arr[i + 1]);
                results.add(temp);
            }
        }

        return results;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = [" + ml.intArrayToString(arr) + "]");

        long start = System.currentTimeMillis();

        List<List<Integer>> result = minimumAbsDifference(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
