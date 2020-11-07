import java.util.*;

public class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        // 8ms
        boolean[] visited = new boolean[n];
        for (int i = 0; i < edges.size(); i++) {
            visited[edges.get(i).get(1)] = true;
        }

        List<Integer> ans = new ArrayList<>();
        for (int j = 0; j < visited.length; j++) {
            if (!visited[j]) {
                ans.add(j);
            }
        }

        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim().split("\\],\\[\\[");

        int n = Integer.parseInt(flds[0].replace("[[", ""));
        System.out.println("n = " + Integer.toString(n));

        String[] str_edges = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<Integer>> edges = ml. stringArrayToListListIntArray(str_edges);
        System.out.println("edges = " + ml.listListIntArrayToString(edges));

        long start = System.currentTimeMillis();

        List<Integer> result = findSmallestSetOfVertices(n, edges);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
