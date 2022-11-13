import java.util.ArrayList;

public class OperateNode {
    public Node createNode(String[] flds) {
        ArrayList<Node> nodes = new ArrayList<>();
        for (String fld : flds) {
            String[] temp = fld.split(",");
            nodes.add(new Node(Integer.parseInt(temp[0])));
        }
        Node head = nodes.get(0);
        Node cur = head;
        for (int i = 0; ; i++) {
            String[] temp = flds[i].split(",");
            if (!temp[1].equals("null")) {
                cur.random = nodes.get(Integer.parseInt(temp[1]));
            }
            if (i == nodes.size() - 1) {
                break;
            }
            cur.next = nodes.get(i + 1);
            cur = cur.next;
        }
        return head;
    }

    public String nodeToString(Node head) {
        if (head == null) {
            return "";
        }
        ArrayList<int[]> flds = nodeToListIntArray(head);
        Mylib ml = new Mylib();
        StringBuilder sb = new StringBuilder(ml.intArrayToString(flds.get(0)));
        for (int i = 1; i < flds.size(); i++) {
            sb.append(", " + ml.intArrayToString(flds.get(i)));
        }
        return sb.toString().replace("-1", "null");
    }
    
    public ArrayList<int[]> nodeToListIntArray(Node head) {
        ArrayList<Node> nodes = new ArrayList<>();
        Node cur = head;
        while (cur != null) {
            nodes.add(cur);
            cur = cur.next;
        }
        ArrayList<int[]> flds = new ArrayList<>();
        cur = head;
        while (cur != null) {
            flds.add(new int[] {cur.val, findNodeIndex(nodes, cur.random)});
            cur = cur.next;
        }
        return flds;
    }

    private int findNodeIndex(ArrayList<Node> nodes, Node target) {
        if (target == null) {
            return -1;
        }
        for (int i = 0; i < nodes.size(); i++) {
            if (target == nodes.get(i)) {
                return i;
            }
        }
        return -1;
    }
}
