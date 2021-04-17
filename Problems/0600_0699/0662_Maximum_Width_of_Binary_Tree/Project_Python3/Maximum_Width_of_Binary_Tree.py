# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # 60ms
        width = []
        def dfs(node: TreeNode, id: int, depth: int):
            if node is None:
                return 0
            if depth >= len(width):
                width.append(id)
            return max(id + 1 - width[depth], max(dfs(node.left, id*2, depth + 1), dfs(node.right, id*2 + 1, depth + 1)))
        return dfs(root, 1, 0)
    
    def widthOfBinaryTree2(self, root: TreeNode) -> int:
        # 40ms
        width = 0
        level = [(1, root)]
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [
                        kid
                        for number, node in level
                        for kid in enumerate((node.left, node.right), 2*number)
                        if kid[1]
                    ]
        return width

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    ope_t = OperateTreeNode()
    t = ope_t.createTreeNode(flds)
    print("t = \n{0}".format(ope_t.treeToStaircaseString(t)))
#   print("t = {0}".format(ope_t.tree2str(t)))

    sl = Solution()
    time0 = time.time()

    result = sl.widthOfBinaryTree(t)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
