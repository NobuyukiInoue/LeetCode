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
}
