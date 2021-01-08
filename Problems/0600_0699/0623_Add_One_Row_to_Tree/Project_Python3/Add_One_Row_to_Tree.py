# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # 56ms
        def addOneRowSub(root: TreeNode, v: int, d: int, n: int, isLeft: bool) -> TreeNode:
            if root is None:
                return None
            if n == d:
                temp = root
                root = TreeNode(v)
                if isLeft:
                    root.left = temp
                else:
                    root.right = temp
            if root.left is not None:
                root.left = addOneRowSub(root.left, v, d, n + 1, True)
            elif n + 1 == d:
                root.left = TreeNode(v)
            if root.right is not None:
                root.right = addOneRowSub(root.right, v, d, n + 1, False)
            elif n + 1 == d:
                root.right = TreeNode(v)
            return root
        return addOneRowSub(root, v, d, 1, True)

    def addOneRow2(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # 48ms
        if d == 1:
            n = TreeNode(v)
            n.left = root
            return n
        dep = 1
        q = [root]
        while dep != d-1:
            newq = []
            for n in q:
                if n.left:
                    newq.append(n.left)
                if n.right:
                    newq.append(n.right)
            q = newq
            dep += 1
        for n in q:
            l, r = n.left, n.right
            newl, newr = TreeNode(v), TreeNode(v)
            newl.left, newr.right = l, r
            n.left, n.right = newl, newr
        return root


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
    v, d = int(flds[1]), int(flds[2])

    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))
    print("v = {0:d}, d = {1:d}".format(v, d))

    sl = Solution()
    time0 = time.time()

    result = sl.addOneRow(root, v, d)

    time1 = time.time()

    print()
    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
