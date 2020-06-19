import java.util.*;

public class Solution {
    TreeNode firstElement;
    TreeNode secondElement;
    TreeNode prevElement;
    
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        // 0ms
        TreeNode node = t1;
        if (t1 == null) {
            node=t2;
        }
        else if (t2 != null) {
            node.val +=t2.val;
            node.left = mergeTrees(t1.left, t2.left);
            node.right = mergeTrees(t1.right, t2.right);
        }
        return node;
    }

    public TreeNode mergeTrees2(TreeNode t1, TreeNode t2) {
        if (t1 == null &&  t2 == null) {
            return null;
        } else if (t1 != null && t2 != null) {
            TreeNode node = new TreeNode(t1.val + t2.val);
            node.left = mergeTrees(t1.left, t2.left);
            node.right = mergeTrees(t1.right, t2.right);
            return node;
        } else if (t1 != null) {
            TreeNode node = new TreeNode(t1.val);
            node.left = mergeTrees(t1.left, null);
            node.right = mergeTrees(t1.right, null);
            return node;
        } else if (t2 != null) {
            TreeNode node = new TreeNode(t2.val);
            node.left = mergeTrees(null, t2.left);
            node.right = mergeTrees(null, t2.right);
            return node;
        } else {
            return null;
        }        
    }

    public void Main(String args) {
        args = args.replaceAll("#.*", "");
        args = args.replaceAll("//.*", "");
        if (args.length() == 0)
            return;

        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode t1 = ope_t.createTreeNode(flds[0]);
        TreeNode t2 = ope_t.createTreeNode(flds[1]);
    //  Codec codec = new Codec();
    //  TreeNode t1 = codec.deserialize(flds[0]);
    //  TreeNode t2 = codec.deserialize(flds[1]);
        System.out.print("t1 = \n" + ope_t.treeToStaircaseString(t1));
        System.out.println("t1 = " + ope_t.tree2str(t1));
        System.out.print("t2 = \n" + ope_t.treeToStaircaseString(t2));
        System.out.println("t2 = " + ope_t.tree2str(t2));

        long start = System.currentTimeMillis();

        TreeNode result = mergeTrees(t1, t2);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
