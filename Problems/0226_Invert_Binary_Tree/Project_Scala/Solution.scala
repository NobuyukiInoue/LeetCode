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

    def print_int_array(nums:Array[Int]):String = {
        if (nums.size <= 0)
            return ""

        var resultStr:String = nums(0).toString
        for (i <- 1 until nums.length) {
            resultStr += ", " + nums(i).toString
        }

        return resultStr
    }

    def main(args:String) {
        var flds:Array[String] = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[", "").replaceFirst("\\]", "").split(",")
        var root:TreeNode = Operate_TreeNode.set_TreeNode(flds);
        println("root = \n" + Operate_TreeNode.output_TreeNode(root))
        println("root = " + Operate_TreeNode.tree2str(root))

        val time_start = System.currentTimeMillis

        var result:TreeNode = invertTree(root)

        val time_end = System.currentTimeMillis

        println("result = \n" + Operate_TreeNode.output_TreeNode(result))
        println("result = " + Operate_TreeNode.tree2str(result))
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
