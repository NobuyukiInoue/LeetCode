from .Node import Node

class OperateNode:
    def createNode(self, flds):
        return self.createSubNode(flds.split(","), 0, 0)

    def createSubNode(self, flds, depth, pos):
        if len(flds) <= 0:
            return None

        cur_pos = 0
        for i in range(depth):
            cur_pos += 2 ** i
        
        if cur_pos + pos > len(flds) - 1:
            return None

        if flds[cur_pos + pos] == 'null':
            return None

        node = Node(int(flds[cur_pos + pos]))
        node.left = self.createSubNode(flds, depth + 1, 2*pos)
        node.right = self.createSubNode(flds, depth + 1, 2*pos + 1)

        return node

    def treeToStaircaseString(self, node):
        self.resultList = []
        self.getStaircaseSubString(node, 0)
        return self.resultListToString()

    def getStaircaseSubString(self, node, n):
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

    def treeToStaircaseString_with_next(self, node):
        self.resultList = []
        self.getStaircaseSubString_with_next(node, 0)
        return self.resultListToString()

    def getStaircaseSubString_with_next(self, node, n):
        if node is None:
            return
        if len(self.resultList) <= n:
            self.resultList.append("(" + str(node.val) + ")")
        else:
            self.resultList[n] += ",(" + str(node.val) + ")"
        if node.next is None:
            self.resultList[n] += ",(#)"
        if node.left is not None:
            self.getStaircaseSubString_with_next(node.left, n + 1)
        if node.right is not None:
            self.getStaircaseSubString_with_next(node.right, n + 1)
        return

    def resultListToString(self):
        resultStr = ""
        for i in range(len(self.resultList)):
            resultStr += self.resultList[i] + "\n"
        self.resultList.clear()
        return resultStr

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""

        resultStr = str(t.val)

        if t.left is None and t.right is None:
            return resultStr

        resultStr += "(" + self.tree2str(t.left) + ")"
        if t.right is not None:
            resultStr += "(" + self.tree2str(t.right) + ")"

        return resultStr
