object Solution {
    def convertBST(root: TreeNode): TreeNode = {
        var sum = 0
        def helper(root: TreeNode): Unit = root match {
        case null => ()
        case r =>
            helper(r.right)
            r.value += sum
            sum = r.value
            helper(r.left)
        }
        helper(root)
        root
    }

    def print_int_array(nums:Array[Int]):String = {
        if (nums.size <= 0)
            return ""

        var resultStr:String = nums(0).toString
        for (i <- 1 until nums.length) {
            resultStr += ", " + nums(i).toString
        }

        return resultStr
    }

    def main(args:String): Unit = {
        var flds:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[", "").replaceFirst("\\]", "")

        var root:TreeNode = OperateTreeNode.createTreeNode(flds);
        print("root = \n" + OperateTreeNode.treeToStaircaseString(root))
        println("root = " + OperateTreeNode.tree2str(root))

        val time_start = System.currentTimeMillis

        var result:TreeNode = convertBST(root)

        val time_end = System.currentTimeMillis

        print("result = \n" + OperateTreeNode.treeToStaircaseString(result))
        println("result = " + OperateTreeNode.tree2str(result))
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
