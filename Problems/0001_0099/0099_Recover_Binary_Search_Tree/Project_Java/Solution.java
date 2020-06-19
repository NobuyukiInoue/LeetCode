import java.util.*;

public class Solution {
    TreeNode firstElement;
    TreeNode secondElement;
    TreeNode prevElement;
    
    public void recoverTree(TreeNode root) {
        // 2ms
        traverse(root);
        int temp = firstElement.val;
        firstElement.val = secondElement.val;
        secondElement.val = temp;
    }
    
    private void traverse(TreeNode root) {
        if (root == null) return;
        
        traverse(root.left);
        if (prevElement != null) {
            if (root.val <= prevElement.val) {
                if (firstElement == null) {
                    firstElement = prevElement;
                    secondElement = root;
                } else {
                    secondElement = root;
                }
            }
        }
        prevElement = root;
        traverse(root.right);
    }

    public void Main(String args) {
        args = args.replaceAll("#.*", "");
        args = args.replaceAll("//.*", "");
        if (args.length() == 0)
            return;

        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds);
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        recoverTree(root);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("result = " + ope_t.tree2str(root));
        System.out.println((end - start)  + "ms\n");
    }
}
