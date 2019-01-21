object OutputTreeNode {
    var resultStr:Array[String] = Array.empty

    def output(node:TreeNode):String = {
        output_tree(node, 0);
        return print_result();
    }

    def output_tree(node:TreeNode, n:Int) {
        if (node == null)
            return
        
        if (resultStr.size <= n) {
            resultStr = resultStr :+ "(" + node.value.toString() + ")"
        } else
            resultStr(n) = resultStr(n) + ",(" + node.value.toString() + ")"

        if (node.left != null)
            output_tree(node.left, n + 1)
        if (node.right != null)
            output_tree(node.right, n + 1)

        return
    }

    def print_result():String = {
        var outputStr:String = ""

        for (temp_str <- resultStr) {
            outputStr = outputStr + temp_str + "\n"
        }

        resultStr = Array.empty
        return outputStr
    }
}
