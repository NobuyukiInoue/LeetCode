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

        var result:Int = findTilt(root)

        val time_end = System.currentTimeMillis

        println("result = " + result )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
