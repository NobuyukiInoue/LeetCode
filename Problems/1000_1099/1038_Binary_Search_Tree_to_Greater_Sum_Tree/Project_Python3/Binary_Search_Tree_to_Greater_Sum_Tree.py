# coding: utf-8

import os
import re
import sys
import time
from typing import Optional, List, Dict, Tuple

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 36ms - 38ms
        self.sum = 0
        self.reverseInorderTraversal(root)
        return root

    def reverseInorderTraversal(self, node: TreeNode):
        if not node:
            return
        self.reverseInorderTraversal(node.right)
        self.sum += node.val
        node.val = self.sum
        self.reverseInorderTraversal(node.left)

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
    temp = re.sub('#.*', "", temp)
    temp = re.sub('//.*', "", temp)
    if len(temp) == 0:
        return

    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds.split(","))
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.bstToGst(root)

    time1 = time.time()

    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
