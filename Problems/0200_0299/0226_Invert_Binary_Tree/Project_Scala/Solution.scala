object Solution {
    def invertTree(root: TreeNode): TreeNode = {
        if (root == null)
            return null
        var t:TreeNode = root.left
        root.left = root.right
        root.right = t
        invertTree(root.left)
        invertTree(root.right)
        return root
    }

    def main(args:String): Unit = {
        var flds:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[", "").replaceFirst("\\]", "")
        var root:TreeNode = OperateTreeNode.createTreeNode(flds);
        println("root = \n" + OperateTreeNode.treeToStaircaseString(root))
        println("root = " + OperateTreeNode.tree2str(root))

        val time_start = System.currentTimeMillis

        var result:TreeNode = invertTree(root)

        val time_end = System.currentTimeMillis

        println("result = \n" + OperateTreeNode.treeToStaircaseString(result))
        println("result = " + OperateTreeNode.tree2str(result))
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
