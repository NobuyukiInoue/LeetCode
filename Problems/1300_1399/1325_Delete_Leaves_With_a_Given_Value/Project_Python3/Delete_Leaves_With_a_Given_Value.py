# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        # 52ms
        if root is None:
            return None
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        if root.val == target and root.left is None and root.right is None:
            root = None
        return root

    def removeLeafNodes2(self, root: TreeNode, target: int) -> TreeNode:
        # 52ms
        def dfs(node: TreeNode):
            if node is None:
                return None
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)
            if node.val == target and node.left is None and node.right is None:
                node = None
            return node
        return dfs(root)

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
    target = int(flds[1])

    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))
    print("target = {0:d}\n".format(target))

    sl = Solution()
    time0 = time.time()

    result = sl.removeLeafNodes(root, target)

    time1 = time.time()

    cd = Codec()

    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("result = [{0}]".format(cd.serialize(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
