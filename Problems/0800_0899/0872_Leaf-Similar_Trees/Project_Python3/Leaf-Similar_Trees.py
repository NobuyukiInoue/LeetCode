# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    def leafSimilar(self, root1, root2):
        def dfs(node, arr):
            if node:
                if not node.left and not node.right: arr += [node.val]
                dfs(node.left, arr)
                dfs(node.right, arr)
                return arr
        return dfs(root1, []) == dfs(root2, [])

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

    root1 = ope_t.createTreeNode(flds[0])
    print("root1 = \n{0}".format(ope_t.treeToStaircaseString(root1)))
    print("root1 = {0}".format(ope_t.tree2str(root1)))

    root2 = ope_t.createTreeNode(flds[1])
    print("root2 = \n{0}".format(ope_t.treeToStaircaseString(root2)))
    print("root2 = {0}".format(ope_t.tree2str(root2)))

    sl = Solution()
    time0 = time.time()

    result = sl.leafSimilar(root1, root2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
