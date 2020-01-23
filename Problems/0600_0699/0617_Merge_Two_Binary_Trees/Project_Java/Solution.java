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

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode t1 = ope_t.set_TreeNode(flds[0].split(","));
        System.out.print("t1 = \n" + ope_t.output_TreeNode(t1));
        System.out.println("t1 = " + ope_t.Tree2str(t1));

        TreeNode t2 = ope_t.set_TreeNode(flds[1].split(","));
        System.out.print("t2 = \n" + ope_t.output_TreeNode(t2));
        System.out.println("t2 = " + ope_t.Tree2str(t2));

        long start = System.currentTimeMillis();

        TreeNode result = mergeTrees(t1, t2);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.output_TreeNode(result));
        System.out.println("result = " + ope_t.Tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
