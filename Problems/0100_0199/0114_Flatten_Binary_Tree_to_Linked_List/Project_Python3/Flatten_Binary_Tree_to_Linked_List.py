# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def flatten(self, root: TreeNode) -> None:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 40ms
        if not root:
            return
        self.prev = root
        self.flatten(root.left)

        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp

        self.flatten(temp)

    def flatten_work(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        # 40ms
        if not root:
            return
        self.results = []
        self.getval(root)
        self.setval(root)

    def getval(self, node):
        self.results.append(node.val)
        if node.left:
            self.getval(node.left)
        if node.right:
            self.getval(node.right)

    def setval(self, node):
        for i in range(len(self.results)):
            node.val = self.results[i]
            node.left = None
            if not node.right and i < len(self.results) - 1:
                node.right = TreeNode(0)
            node = node.right

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

    sl.flatten(root)

    time1 = time.time()

    print("result = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("result = {0}".format(ope_t.tree2str(root)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
