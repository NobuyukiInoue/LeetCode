from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder_submission(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while(queue):
            levelRes = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                levelRes.append(curr.val)
                queue.extend(curr.children)
            result.append(levelRes)
        return result

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        llist = [[]]
        temp = []

        if root is None:
            return temp
        
        temp.append(root.val)
        llist[0] = temp

        for i in range(0, len(root.children)):
            self.nextOrder(root.children[i], llist, 1)
        
        return llist
    
    def nextOrder(self, node, llist, n):
        if node is None:
            return
        
        if len(llist) > n:
            llist[n].append(node.val)
        else:
            curr_list = []
            curr_list.append(node.val)
            llist.append(curr_list)
        
        if node.children is None:
            return
        
        for i in range(0, len(node.children)):
            self.nextOrder(node.children[i], llist, n + 1)
    
    def outputOrder(self, llist):
        resultStr = ""
        for i in range(0, len(llist)):
            resultStr += "["
            for j in range(0, len(llist[i])):
                if j < len(llist[i]) - 1:
                    resultStr += str(llist[i][j]) + ","
                else:
                    resultStr += str(llist[i][j])
        resultStr += "]\n"
        return resultStr

    def set_node(self):
        n1_list = []
        n1_list.append(Node(5, None))
        n1_list.append(Node(6, None))

        n0_list = []
        n0_list.append(Node(3, n1_list))
        n0_list.append(Node(2, None))
        n0_list.append(Node(4, None))

        node = Node(1, n0_list)
        return node
        
    def output_node(self, node):
        if node is None:
            return ""
        
        self.resultStr = []
        self.resultStr.append(str(node.val))
        self.set_output_node(node, 1)

        if len(self.resultStr) <= 0:
            return ""

        result = "[\n"
        for i in range(0, len(self.resultStr)):
            if i < len(self.resultStr) - 1:
                result += "\t[" + self.resultStr[i] + "],\n"
            else:
                result += "\t[" + self.resultStr[i] + "]\n"
        result += "]"

        return result
                
    def set_output_node(self, node, n):
        if node.children is None:
            return

        tempStr = ""
        for i in range(0, len(node.children)):
            if i == 0:
                tempStr += str(node.children[i].val)
            else:
                tempStr += "," + str(node.children[i].val)

        if len(self.resultStr) <= n:
            self.resultStr.append(tempStr)
        else:
            self.resultStr[n] += tempStr

        for i in range(0, len(node.children)):
            self.set_output_node(node.children[i], n + 1)

def main():
    sl = Solution()
    node = sl.set_node()
    print("{0}".format(sl.output_node(node)))
    llist = sl.levelOrder(node)
    #print("{0}".format(sl.outputOrder(llist)))
    print(llist)

if __name__ == "__main__":
    main()
