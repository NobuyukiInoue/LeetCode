object Solution {
    def tree2str(t: TreeNode): String = {
        if (t == null)
            return ""

        var resultStr:String = t.value.toString

        if (t.left == null && t.right == null)
            return resultStr

        resultStr += "(" + tree2str(t.left) + ")"
        if (t.right != null)
            resultStr += "(" + tree2str(t.right) + ")"

        return resultStr
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
        var t:TreeNode = Operate_TreeNode.set_TreeNode(flds);
        println("t = \n" + Operate_TreeNode.output_TreeNode(t))

        val time_start = System.currentTimeMillis

        var result:String = tree2str(t)

        val time_end = System.currentTimeMillis

        println("result = " + result )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
