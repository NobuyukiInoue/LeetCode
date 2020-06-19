object Solution {
    var tilt:Int = 0

    def findTilt(root: TreeNode): Int = {
        tilt = 0
        var sum:Int = returnSum(root)
        return tilt
    }
    
    def returnSum(root:TreeNode): Int = {
        if (root == null)
            return 0
        var left:Int = returnSum(root.left)
        var right:Int = returnSum(root.right)
        tilt += IntAbs(left - right)
        return root.value + left + right
    }

    def IntAbs(x:Int): Int = {
        if (x >= 0)
            return x
        else
            return -x
    }

    def main(args:String): Unit = {
        var flds:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[", "").replaceFirst("\\]", "")
        var root:TreeNode = OperateTreeNode.createTreeNode(flds);
        println("root = \n" + OperateTreeNode.treeToStaircaseString(root))
        println("root = " + OperateTreeNode.tree2str(root))

        val time_start = System.currentTimeMillis

        var result:Int = findTilt(root)

        val time_end = System.currentTimeMillis

        println("result = " + result )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
