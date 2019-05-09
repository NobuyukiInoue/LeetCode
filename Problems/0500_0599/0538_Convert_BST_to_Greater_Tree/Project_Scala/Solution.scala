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

    def main(args:String) {
        var nums_str1:Array[String] = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[", "").replaceFirst("\\]", "").split(",")

        var root:TreeNode = Operate_TreeNode.set_TreeNode(nums_str1);
        print("root = \n" + Operate_TreeNode.output_TreeNode(root))
        println("root = " + Operate_TreeNode.tree2str(root))

        val time_start = System.currentTimeMillis

        var result:TreeNode = convertBST(root)

        val time_end = System.currentTimeMillis

        print("result = \n" + Operate_TreeNode.output_TreeNode(result))
        println("result = " + Operate_TreeNode.tree2str(result))
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
