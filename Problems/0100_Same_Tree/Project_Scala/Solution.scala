object Solution {
    def isSameTree(p: TreeNode, q: TreeNode): Boolean = {
        if (p == null && q == null) return true
        if (p == null || q == null) return false

        p._value == q._value && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
    }

    def isSameTree_work(p: TreeNode, q: TreeNode): Boolean = {
        if (p == null && q == null) {
            return true;
        }
        else if (p == null || q == null)
        {
            return false;
        }

        if (p.value == q.value) {
            if (isSameTree(p.left, q.left)) {
                return isSameTree(p.right, q.right)
            }
            else {
                return false
            }
        }
        else {
            return false
        }
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

        var p:TreeNode = Operate_TreeNode.set_TreeNode(nums_str1);
        var q:TreeNode = Operate_TreeNode.set_TreeNode(nums_str2);
        print("p = \n" + Operate_TreeNode.output_TreeNode(p))
        println("p = " + Operate_TreeNode.tree2str(p))
        print("q = \n" + Operate_TreeNode.output_TreeNode(q))
        println("q = " + Operate_TreeNode.tree2str(q))

        val time_start = System.currentTimeMillis

        var result: Boolean = isSameTree(p, q)

        val time_end = System.currentTimeMillis

        println("result = " + result.toString )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
