import java.util.Enumeration;

public class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // 2ms
        return helper(0, 0, inorder.length - 1, preorder, inorder);
    }

    private TreeNode helper(int preStart, int inStart, int inEnd, int[] preorder, int[] inorder) {
        if (preStart > preorder.length - 1 || inStart > inEnd)
            return null;
        
        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = 0;

        for (int i = 0; i <= inEnd; i++) {
            if (inorder[i] == root.val) {
                inIndex = i;
            }
        }

        root.left = helper(preStart + 1, inStart, inIndex - 1, preorder, inorder);
        root.right = helper(preStart + inIndex - inStart + 1, inIndex + 1, inEnd, preorder, inorder);
        return root;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String[] nums1 = flds[0].split(",");
        String[] nums2 = flds[1].split(",");

        int[] preorder = new int[nums1.length];
        for (int i = 0; i < preorder.length; ++i) {
            preorder[i] = Integer.parseInt(nums1[i]);
        }

        int[] inorder = new int[nums2.length];
        for (int i = 0; i < inorder.length; ++i) {
            inorder[i] = Integer.parseInt(nums2[i]);
        }

        Mylib ml = new Mylib();
        System.out.println("preorder = " + ml.intArrayToString(preorder));
        System.out.println("inorder = " + ml.intArrayToString(inorder));

        long start = System.currentTimeMillis();

        TreeNode result = buildTree(preorder, inorder);

        long end = System.currentTimeMillis();

        OperateTreeNode ope_t = new OperateTreeNode();
        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));

        System.out.println((end - start)  + "ms\n");
    }
}
