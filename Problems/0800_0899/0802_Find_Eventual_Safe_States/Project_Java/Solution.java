import java.util.*;

public class Solution {
/*
    Boolean[] memo;
    public List<Integer> eventualSafeNodes(int[][] graph) {
        // 4ms
        memo = new Boolean[graph.length];
        List<Integer> result = new LinkedList<>();
        for (int i = 0; i < graph.length; i++) {
            if (canJump(graph, i)) {
                result.add(i);
            }
        }
        return result;
    }
    
    boolean canJump(int[][] graph, int node) {
        if (memo[node] != null) {
            return memo[node];
        }
        memo[node] = false;
        for (int child : graph[node]) {
            if (!canJump(graph, child)) {
                return false;
            }
        }
        memo[node] = true;
        return memo[node];
    }
*/
    public List<Integer> eventualSafeNodes(int[][] graph) {
        // 6ms
        int n = graph.length;
        boolean[] visited = new boolean[n];
        boolean[] recStack = new boolean[n];
        boolean[] nodeInCycle = new boolean[n];
        List<Integer> res = new ArrayList<>();
        for (int i = 0 ; i < n; i++) {
            if (!visited[i]) {
                checkIfNodeIsSafe(graph, nodeInCycle, visited, recStack, i, n);
            }
        }
        for (int i = 0; i < n; i++) {
            if (!nodeInCycle[i]) {
                res.add(i);
            }
        }
        return res;
    }

    public boolean checkIfNodeIsSafe(int[][] graph, boolean[] nodeInCycle, boolean[] visited, boolean[] recStack, int i, int n){
        if (recStack[i]) {
            nodeInCycle[i] = true;
            return false;
        }
        
        if (visited[i]) {
            return true;
        }
        
        visited[i] = true;
        recStack[i] = true;
        
        for (int j : graph[i]) {
            if (!checkIfNodeIsSafe(graph, nodeInCycle, visited, recStack, j, n)) {
                nodeInCycle[i] = true;
                return false;
            }
        }
        nodeInCycle[i] = false;
        recStack[i] = false;
        return true;
    }

    private String[] mySplit(String flds) {
        int pos = 0;
        List<String> res = new ArrayList<>();
        while (pos < flds.length()) {
            pos = flds.indexOf("],[");
            res.add(flds.substring(0, pos));
            flds = flds.substring(pos + 3);
        }
        res.add(flds);
        return res.toArray(new String[0]);
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
//      String[] str_graph = flds.split("\\],\\[");
        String[] str_graph = mySplit(flds);
        Mylib ml = new Mylib();
        int[][] graph = ml.stringToIntIntArray(str_graph);
        for (int i = 0; i < graph.length; i++) {
            if (graph[i] == null) {
                graph[i] = new int[0];
            }
        }
        System.out.println("graph = " + ml.intIntArrayToString(graph));

        long start = System.currentTimeMillis();

        List<Integer> result = eventualSafeNodes(graph);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
