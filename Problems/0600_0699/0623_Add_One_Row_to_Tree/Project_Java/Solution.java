import java.util.*;

public class Solution {
    public TreeNode addOneRow(TreeNode root, int v, int d) {
        // 1ms
        return addOneRow(root, v, d, 1, true);
    }

    public TreeNode addOneRow(TreeNode root, int v, int d, int n, boolean isLeft) {
        if (root == null)
            return null;
        if (n == d) {
            TreeNode temp = root;
            root = new TreeNode(v);
            if (isLeft) {
                root.left = temp;
            } else {
                root.right = temp;
            }
        }
        if (root.left != null) {
            root.left = addOneRow(root.left, v, d, n + 1, true);
        } else if (n + 1 == d) {
            root.left = new TreeNode(v);
        }
        if (root.right != null) {
            root.right = addOneRow(root.right, v, d, n + 1, false);
        } else if (n + 1 == d) {
            root.right = new TreeNode(v);
        }
        return root;
    }

    public TreeNode addOneRow2(TreeNode root, int v, int d) {
        // 1ms
        if (d == 1) {
            TreeNode n = new TreeNode(v);
            n.left = root;
            return n;
        }
        int dep = 1;
        List<TreeNode> q = new ArrayList<>();
        q.add(root);
        while (dep != d - 1) {
            List<TreeNode> newq = new ArrayList<>();
            for (TreeNode n : q) {
                if (n.left != null) {
                    newq.add(n.left);
                }
                if (n.right != null) {
                    newq.add(n.right);
                }
            }
            q = newq;
            dep++;
        }
        for (TreeNode n : q) {
            TreeNode l = n.left;
            TreeNode r = n.right;
            TreeNode newl = new TreeNode(v);
            TreeNode newr = new TreeNode(v);
            newl.left = l;
            newr.right = r;
            n.left = newl;
            n.right = newr;
        }
        return root;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds[0]);
    //  Codec codec = new Codec();
    //  TreeNode p = codec.deserialize(flds[0]);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));
        int v = Integer.parseInt(flds[1]);
        int d = Integer.parseInt(flds[2]);
        System.out.println("v = " + Integer.toString(v) + ", d = " + Integer.toString(d));

        long start = System.currentTimeMillis();

        TreeNode result = addOneRow2(root, v, d);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
