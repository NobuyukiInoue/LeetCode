public class Solution {
    int tilt = 0;
    public int findTilt(TreeNode root) {
        tilt = 0;
        int sum = returnSum(root);
        return tilt;
    }
    
    public int returnSum(TreeNode root){
        if(root==null)
            return 0;
        int left = returnSum(root.left);
        int right = returnSum(root.right);
        tilt += Math.abs(left-right);
        return root.val + left + right;
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

        int result = findTilt(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
