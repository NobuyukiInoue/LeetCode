import java.util.*;

public class Solution {
    Set<Integer> to_delete_set;
    List<TreeNode> res;

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        // 2ms
        to_delete_set = new HashSet<>();
        res = new ArrayList<>();
        for (int i : to_delete)
            to_delete_set.add(i);
        helper(root, true);
        return res;
    }

    private TreeNode helper(TreeNode node, boolean is_root) {
        if (node == null)
            return null;
        boolean deleted = to_delete_set.contains(node.val);
        if (is_root && !deleted)
            res.add(node);
        node.left = helper(node.left, deleted);
        node.right =  helper(node.right, deleted);
        return deleted ? null : node;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds[0]);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        Mylib ml = new Mylib();
        int[] to_delete = ml.stringToIntArray(flds[1]);
        System.out.println("to_delete = " + ml.intArrayToString(to_delete) + "\n");

        long start = System.currentTimeMillis();

        List<TreeNode> result = delNodes(root, to_delete);

        long end = System.currentTimeMillis();

        Codec codec = new Codec();
        for (int i = 0; i < result.size(); i++) {
            if (i == 0)
                System.out.print("result = [[" + codec.serialize(result.get(i)) + "]");
            else
                System.out.print(",[" + codec.serialize(result.get(i)) + "]");
        }
        System.out.println("]");

        for (int i = 0; i < result.size(); i++) {
            System.out.print("result[" + Integer.toString(i) + "] = \n" + ope_t.treeToStaircaseString(result.get(i)));
        }
        System.out.println();

        for (int i = 0; i < result.size(); i++) {
            System.out.println("result[" + Integer.toString(i) + "] = " + ope_t.tree2str(result.get(i)));
        }
        System.out.println();

        System.out.println((end - start)  + "ms\n");
    }
}
