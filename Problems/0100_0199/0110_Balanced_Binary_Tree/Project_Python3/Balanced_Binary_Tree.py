# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def isBalanced(self, root: TreeNode) -> bool:
    def isBalanced(self, root):
        # 56ms
        if not root:
            return True
        def depth(node):
            if not node:    #leaves
                return 0
            left = depth(node.left) #left child's depth
            right = depth(node.right) #right child's depth
            if abs(left-right)>1:
                raise Exception #stop recursion and report unbalance
            return max(left, right)+1
        try:
            return abs(depth(root.left)-depth(root.right))<=1
        except:
            return False

    def isBalanced2(self, root):
        # 70ms
        def getNodeDepth(node):
            if node is None:
                return 0
            stack = [(node,1)]
            dep = 1
            while(len(stack)):
                first,dep=stack.pop(0)
                if first.left is not None:
                    stack.append((first.left,dep+1))
                if first.right is not None:
                    stack.append((first.right,dep+1))
            return dep
        if root is None:
            return True
        l = getNodeDepth(root.left)
        r = getNodeDepth(root.right)
        return abs(l-r) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").rstrip()

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds.split(","))
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.isBalanced(root)

    time1 = time.time()

    ope_t = OperateTreeNode()
    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
