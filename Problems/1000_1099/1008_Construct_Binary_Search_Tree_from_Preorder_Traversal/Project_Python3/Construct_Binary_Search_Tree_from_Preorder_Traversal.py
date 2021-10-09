# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode
from typing import List, Dict, Tuple, Optional

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # 24ms
        if preorder is None:
            return None

        def helper(node: TreeNode, val: int):
            if node is None:
                node = TreeNode(val)
                return node
            if val < node.val:
                node.left = helper(node.left, val)
            else:
                node.right = helper(node.right, val)
            return node

        node = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            helper(node, preorder[i])
        return node

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

    preorder = [int(fld) for fld in flds.split(",")]
    print("preorder = {0}".format(preorder))

    sl = Solution()
    time0 = time.time()

    result = sl.bstFromPreorder(preorder)

    time1 = time.time()

    ope_t = OperateTreeNode()
    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
