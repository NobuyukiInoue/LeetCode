public class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        // 0ms
        if (root == null)
            return root;
        if (root.val > key) {
            root.left = deleteNode(root.left, key);
        } else if (root.val < key) {
            root.right= deleteNode(root.right, key);
        } else {
            if (root.right == null) {
                return root.left;
            }
            if (root.left == null) {
                return root.right;
            }

            TreeNode temp = root.right;
            int mini = temp.val;
            while (temp.left != null) {
                temp = temp.left;
                mini = temp.val;
            }
            root.val = mini;
            root.right = deleteNode(root.right, root.val);
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
        int key = Integer.parseInt(flds[1]);
        System.out.println("key = " + Integer.toString(key));

        long start = System.currentTimeMillis();

        TreeNode result = deleteNode(root, key);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
