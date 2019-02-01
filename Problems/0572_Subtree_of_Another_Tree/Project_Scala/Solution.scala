object Solution {
    def isSubtree(s: TreeNode, t: TreeNode): Boolean = {
        if (s.value == t.value)
            if (isSameTree(s, t))
                return true;
        if (s.left != null)
            if (isSubtree(s.left, t))
                return true;
        if (s.right != null)
            if (isSubtree(s.right, t))
                return true;
        return false;
    }

    def isSameTree(p: TreeNode, q: TreeNode): Boolean = {
        if (p == null && q == null) return true
        if (p == null || q == null) return false

        p._value == q._value && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
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
        var temp:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[\\[", "").replaceFirst("\\]\\]", "")
        var flds:Array[String] = temp.split("\\],\\[")

        var nums_str1:Array[String] = flds(0).split(",")
        var nums_str2:Array[String] = flds(1).split(",")

        var s:TreeNode = Operate_TreeNode.set_TreeNode(nums_str1, 0, 0);
        var t:TreeNode = Operate_TreeNode.set_TreeNode(nums_str2, 0, 0);
        print("s = \n" + Operate_TreeNode.output_TreeNode(s))
        println("s = \n" + Operate_TreeNode.tree2str(s))
        print("t = \n" + Operate_TreeNode.output_TreeNode(t))
        println("t = \n" + Operate_TreeNode.tree2str(t))

        val time_start = System.currentTimeMillis

        var result: Boolean = isSubtree(s, t)

        val time_end = System.currentTimeMillis

        println("result = " + result.toString )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
