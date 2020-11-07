import java.util.*;

public class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        // 2ms
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();

        path.add(0);
        dfsSearch(graph, 0, res, path);
					
        return res;
    }

    private void dfsSearch(int[][] graph, int node, List<List<Integer>> res, List<Integer> path) {
        if (node == graph.length - 1) {
            res.add(new ArrayList<Integer>(path));
            return;
        }

        for (int nextNode : graph[node]) {
            path.add(nextNode);
            dfsSearch(graph, nextNode, res, path);
            path.remove(path.size() - 1);
        }
    }

    public List<List<Integer>> allPathsSourceTarget2(int[][] graph) {
        // 7ms
        class Node {
            List<Integer> nodes;
            int id;
            Node(int id) {
                this.id = id;
                nodes = new ArrayList<>();
                nodes.add(id);
            }
        }

        List<List<Integer>> res = new ArrayList<>();
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0));

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                Node current = q.poll();
                if (current.id == graph.length - 1) {
                    res.add(new ArrayList<>(current.nodes));
                    continue;
                }
                for (int node: graph[current.id]) {
                    Node n = new Node(node);
                    n.nodes = new ArrayList<>(current.nodes);
                    n.nodes.add(node);
                    q.offer(n);
                }
            }
        }

        return res;
    }

    public int[][] stringToIntIntArray2(Mylib ml, String[] s) {
        if (s == null)
            return null;

        int[][] nums = new int[s.length + 1][];
        for (int i = 0; i < s.length; i++) {
            nums[i] = ml.stringToIntArray(s[i]);
        }

        return nums;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] graph = new int[flds.length][];
        graph = stringToIntIntArray2(ml, flds);
        System.out.println("graph = " + ml.intIntArrayToString(graph));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = allPathsSourceTarget(graph);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
