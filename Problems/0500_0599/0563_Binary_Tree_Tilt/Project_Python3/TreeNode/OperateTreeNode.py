from typing import List, Dict, Tuple

from .TreeNode import TreeNode

class OperateTreeNode:
#   def createTreeNode(self, flds):
    def createTreeNode(self, flds: List[str], depth: int = 0, pos: int = 0) -> TreeNode:
        if pos >= len(flds) or len(flds) <= 0:
            return None
        cur_pos = 0
        for i in range(depth):
            cur_pos += 2 ** i
        if cur_pos + pos > len(flds) - 1:
            return None
        if flds[cur_pos + pos] == 'null':
            return None
        node = TreeNode(int(flds[cur_pos + pos]))
        node.left = self.createTreeNode(flds, depth + 1, 2*pos)
        node.right = self.createTreeNode(flds, depth + 1, 2*pos + 1)
        return node

    def treeToStaircaseString(self, node: TreeNode) -> str:
        self.resultList = []
        self.getStaircaseSubString(node, 0)
        return self.resultListToString()

    def getStaircaseSubString(self, node: TreeNode, n: int) -> None:
        if node is None:
            return
        if len(self.resultList) <= n:
            self.resultList.append("(" + str(node.val) + ")")
        else:
            self.resultList[n] += ",(" + str(node.val) + ")"
        if node.left is not None:
            self.getStaircaseSubString(node.left, n + 1)
        if node.right is not None:
            self.getStaircaseSubString(node.right, n + 1)
        return

    def resultListToString(self) -> str:
        resultStr = "\n".join(self.resultList)
        self.resultList.clear()
        return resultStr

    def tree2str(self, node: TreeNode) -> str:
        """
        :type node: TreeNode
        :rtype: str
        """
        if node is None:
            return ""

        resultStr = str(node.val)

        if node.left is None and node.right is None:
            return resultStr

        resultStr += "(" + self.tree2str(node.left) + ")"
        if node.right is not None:
            resultStr += "(" + self.tree2str(node.right) + ")"

        return resultStr
