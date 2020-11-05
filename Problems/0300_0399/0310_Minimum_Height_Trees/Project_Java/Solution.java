import java.util.*;

public class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        // 11ms
        if (n == 0) {
            return new ArrayList<>();
        } else if (n == 1) {
            List<Integer> ret = new ArrayList<>();
            ret.add(0);
            return ret;
        }
        List<Integer>[] lists = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            lists[i] = new ArrayList<>();
        }
        for (int i = 0; i < edges.length; i++) {
            int v1 = edges[i][0];
            int v2 = edges[i][1];
            lists[v1].add(v2);
            lists[v2].add(v1);
        }
        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (lists[i].size() == 1) {
                leaves.add(i);
            }
        }
        int count = n;
        while (count > 2) {
            int size = leaves.size();
            count -= size;
            List<Integer> newLeaves = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                int leaf = leaves.get(i);
                for (int j = 0; j < lists[leaf].size(); j++) {
                    int toRemove = lists[leaf].get(j);
                    lists[toRemove].remove(Integer.valueOf(leaf));
                    if (lists[toRemove].size() == 1)
                        newLeaves.add(toRemove);
                }
            }
            leaves = newLeaves;
        }
        return leaves;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").trim().split("\\],\\[\\[");

        int n = Integer.parseInt(flds[0].replace("[", ""));
        System.out.println("n = " + Integer.toString(n));

        flds[1] = flds[1].replace("]]]", "");
    //  System.out.println("flds[1] = " + flds[1]);
    //  System.out.println("flds[1].length = " + Integer.toString(flds[1].length()));

        Mylib ml = new Mylib();
        int[][] edges;
        if (flds[0].length() > 0) {
            String[] dataStr = flds[1].split("\\],\\[");
            edges = ml.stringToIntIntArray(dataStr);
            System.out.println("edges = " + ml.matrixToString(edges));
        } else {
            edges = new int[0][0];
            System.out.println("edges = [[]]");
        }

        long start = System.currentTimeMillis();

        List<Integer> result = findMinHeightTrees(n, edges);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
