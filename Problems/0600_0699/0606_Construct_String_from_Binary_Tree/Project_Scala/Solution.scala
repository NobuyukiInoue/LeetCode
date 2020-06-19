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

    def main(args:String): Unit = {
        var flds:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[", "").replaceFirst("\\]", "")
        var t:TreeNode = OperateTreeNode.createTreeNode(flds);
        println("t = \n" + OperateTreeNode.treeToStaircaseString(t))

        val time_start = System.currentTimeMillis

        var result:String = tree2str(t)

        val time_end = System.currentTimeMillis

        println("result = " + result )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
