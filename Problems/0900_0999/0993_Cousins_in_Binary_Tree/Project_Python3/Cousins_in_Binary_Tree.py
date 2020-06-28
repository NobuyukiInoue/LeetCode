# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    def isCousins(self, root, x, y):
        # 28ms
        firstParent = None
        queue = [root]
        while queue:
            nextQueue = []
            for node in queue:
                for nextNode in (node.left, node.right):
                    if nextNode:
                        if nextNode.val in (x, y):
                            if not firstParent:
                                firstParent = node
                            else:
                                return firstParent != node
                        nextQueue.append(nextNode)
            if firstParent:
                return False
            queue = nextQueue

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds[0])
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    x = int(flds[1])
    y = int(flds[2])
    print("x = {0:d}, y = {1:d}".format(x, y))

    sl = Solution()
    time0 = time.time()

    result = sl.isCousins(root, x, y)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
