from .TreeNode import TreeNode

class OperateTreeNode:
    def createTreeNode(self, flds):
        return self.createSubTreeNode(flds.split(","), 0, 0)

    def createSubTreeNode(self, flds, depth, pos):
        if len(flds) <= 0:
            return None

        cur_pos = 0
        for i in range(depth):
            cur_pos += 2 ** i

        if cur_pos + pos > len(flds) - 1:
            return None

        if flds[cur_pos + pos] == 'null':
            return None

        node = TreeNode(int(flds[cur_pos + pos]))
        node.left = self.createSubTreeNode(flds, depth + 1, 2*pos)
        node.right = self.createSubTreeNode(flds, depth + 1, 2*pos + 1)

        return node

    def treeToStaircaseString(self, node):
        self.resultList = []
        self.getStaircaseSubString(node, 0)
        return self.resultListToString()

    def getStaircaseSubString(self, node, n):
        if node == None:
            return
        if len(self.resultList) <= n:
            self.resultList.append("(" + str(node.val) + ")")
        else:
            self.resultList[n] += ",(" + str(node.val) + ")"
        if node.left != None:
            self.getStaircaseSubString(node.left, n + 1)
        if node.right != None:
            self.getStaircaseSubString(node.right, n + 1)
        return

    def resultListToString(self):
        resultStr = "\n".join(self.resultList)
        self.resultList.clear()
        return resultStr

    def tree2str(self, node):
        """
        :type node: TreeNode
        :rtype: str
        """
        if node == None:
            return ""

        resultStr = str(node.val)

        if node.left == None and node.right == None:
            return resultStr

        resultStr += "(" + self.tree2str(node.left) + ")"
        if node.right != None:
            resultStr += "(" + self.tree2str(node.right) + ")"

        return resultStr
