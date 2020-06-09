import java.util.*;

public class Solution_work {
    List<List<Node>> levels;
    List<Integer> pos;

    public Node connect(Node root) {
        // 6ms
        if (root == null)
            return root;

        levels = new ArrayList<>();
        pos = new ArrayList<>();

        get_node(root, 0);
        set_next(root, 0);

        return root;
    }

    private void get_node(Node node, int level) {
        if (levels.size() <= level) {
            List<Node> temp = new ArrayList<>();
            temp.add(node);
            levels.add(temp);
            pos.add(0);
        } else {
            levels.get(level).add(node);
        }
        if (node.left != null) {
            get_node(node.left, level + 1);
        }
        if (node.right != null) {
            get_node(node.right, level + 1);
        }
    }

    private void set_next(Node node, int level) {
        if (levels.get(level).size() > pos.get(level) + 1) {
            node.next = levels.get(level).get(pos.get(level) + 1);
            pos.set(level, pos.get(level) + 1);
        } else {
            node.next = null;
        }
        if (node.left != null) {
            set_next(node.left, level + 1);
        }
        if (node.right != null) {
            set_next(node.right, level + 1);
        }
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        String[] nums = flds.split(",");

        Operate_Node ope_t = new Operate_Node();
        Node root = ope_t.set_Node(nums);
        System.out.print("root = \n" + ope_t.output_Node(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        Node result = connect(root);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.output_Node_with_next(result));
        System.out.println("result = " + ope_t.Tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
