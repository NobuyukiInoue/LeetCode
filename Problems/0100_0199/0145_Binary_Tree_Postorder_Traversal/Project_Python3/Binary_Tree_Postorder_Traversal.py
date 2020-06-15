# coding: utf-8

import os
import re
import sys
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
#   def postorderTraversal(self, root: TreeNode) -> List[int]:
    def postorderTraversal(self, root):
        # 40ms
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node):
        if node == None:
            return
        self.res = [node.val] + self.res[:]
        if node.right != None:
            self.helper(node.right)
        if node.left != None:
            self.helper(node.left)
        return

    def postorderTraversal2(self, root):
        # 28ms
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

class output_TreeNode:
    def output(self, node):
        self.resultStr = []
        self.output_TreeNode(node, 0)
        return self.print_resultStr()

    def output_TreeNode(self, node, n):
        if node == None:
            return
        if len(self.resultStr) <= n:
            self.resultStr.append("(" + str(node.val) + ")")
        else:
            self.resultStr[n] += ",(" + str(node.val) + ")"
        if node.left != None:
            self.output_TreeNode(node.left, n + 1)
        if node.right != None:
            self.output_TreeNode(node.right, n + 1)
        return

    def print_resultStr(self):
        outputStr = ""
        for i in range(len(self.resultStr)):
            outputStr += self.resultStr[i] + "\n"
        self.resultStr.clear()
        return outputStr

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ""

        resultStr = str(t.val)

        if t.left == None and t.right == None:
            return resultStr

        resultStr += "(" + self.tree2str(t.left) + ")"
        if t.right != None:
            resultStr += "(" + self.tree2str(t.right) + ")"

        return resultStr

def set_node(flds, depth, pos):
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
    node.left = set_node(flds, depth + 1, 2*pos)
    node.right = set_node(flds, depth + 1, 2*pos + 1)

    return node

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    temp = re.sub('#.*', "", temp)
    temp = re.sub('//.*', "", temp)
    if len(temp) == 0:
        return
        
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    root = set_node(flds.split(","), 0, 0)

    ol = output_TreeNode()
    print("root = \n{0}".format(ol.output(root)))
    print("root = {0}".format(ol.tree2str(root)))

    time0 = time.time()

    sl = Solution()
    result = sl.postorderTraversal(root)

    time1 = time.time()
    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
