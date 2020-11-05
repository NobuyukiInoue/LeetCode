import java.util.*;

public class Solution {
    public List<List<Integer>> largeGroupPositions(String S) {
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0, j = 0; i < S.length(); i = j) {
            while (j < S.length() && S.charAt(j) == S.charAt(i))
                ++j;
            if (j - i >= 3)
                res.add(Arrays.asList(i, j - 1));
        }
        return res;
    }

    public void Main(String temp) {
        String S = temp.replace("\"", "").replace("[", "").replace("]", "").trim();
        System.out.println("S = " + S);

        long start = System.currentTimeMillis();

        List<List<Integer>> result = largeGroupPositions(S);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
