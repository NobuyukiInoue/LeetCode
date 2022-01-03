import java.util.*;

public class OperateNode {
    public Node createNode(String flds) {
        Mylib ml = new Mylib();
        int[][] data = ml.stringToIntIntArray(flds.split("\\],\\["));
        Node[] nodes = new Node[data.length];
        for (int i = 0; i < data.length; i++) {
            nodes[i] = new Node(i + 1);
        }
        for (int i = 0; i < nodes.length; i++) {
            List<Node> temp = new ArrayList<>();
            for (int val : data[i]) {
                temp.add(nodes[val - 1]);
            }
            nodes[i].neighbors = temp;
        }
        return nodes[0];
    }

    public String nodeToString(Node node) {
        if (node == null) {
            return "[]";
        }

        HashMap<Integer, List<Node>> data = new HashMap<>();
        data.put(node.val, node.neighbors);

        for (Node nei : node.neighbors) {
            data.put(nei.val, nei.neighbors);
            for (Node nei2 : nei.neighbors) {
                if (!data.containsKey(nei2.val)) {
                    data.put(nei2.val, nei2.neighbors);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i : data.keySet()) {
            List<Node> nei = data.get(i);
            if (sb.charAt(sb.length() - 1) == '[') {
                sb.append("[");
            } else {
                sb.append(",[");
            }
            for (Node n : nei) {
                if (sb.charAt(sb.length() - 1) == '[') {
                    sb.append(Integer.toString(n.val));
                } else {
                    sb.append("," + Integer.toString(n.val));
                }
            }
            sb.append("]");
        }
        sb.append("]");
        return sb.toString();
    }
}
