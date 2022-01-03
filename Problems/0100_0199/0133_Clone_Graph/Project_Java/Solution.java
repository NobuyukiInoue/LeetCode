import java.util.*;

public class Solution {
    public Node cloneGraph(Node node) {
        // 24ms
        if (node == null) {
            return null;
        }
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(node);
        Map<Node, Node> map = new HashMap<Node, Node>();
        map.put(node, new Node(node.val));
        while (!queue.isEmpty()) {
            Node temp = queue.poll();
            for (Node neighbor : temp.neighbors) {
                if (!map.containsKey(neighbor)) {
                    map.put(neighbor, new Node(neighbor.val));
                    queue.add(neighbor);
                }
                map.get(temp).neighbors.add(map.get(neighbor));
            }
        }
        return map.get(node);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim();

        OperateNode ope_n = new OperateNode();
        Node node;
        if (flds.equals("[]")) {
            node = new Node();
        } else if (flds.equals("")) {
            node = new Node();
        } else {
            node = ope_n.createNode(flds);
        }
        System.out.println("node = " + ope_n.nodeToString(node));

        long start = System.currentTimeMillis();

        Node result = cloneGraph(node);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope_n.nodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
