//import java.awt.List;
import java.util.*;

public class Solution {
    List<String> result;

    public List<String> binaryTreePaths(TreeNode root) {
        result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        subtree(root, Integer.toString(root.val));
        return result;
    }

    public void subtree(TreeNode node, String path) {
        if (node.left == null && node.right == null) {
            result.add(path);
            return;
        }

        if (node.left != null) {
            subtree(node.left, path + "->" + Integer.toString(node.left.val));
        }

        if (node.right != null) {
            subtree(node.right, path + "->" + Integer.toString(node.right.val));
        }
    }

    public void list_Array2String(List<String> ll) {
        for (int i = 0; i < ll.size(); i++) {
            System.out.println(ll.get(i));
        }
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds);
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        List<String> result = binaryTreePaths(root);

        long end = System.currentTimeMillis();

        System.out.println("result = ");
        list_Array2String(result);
        System.out.println((end - start)  + "ms\n");
    }
}
