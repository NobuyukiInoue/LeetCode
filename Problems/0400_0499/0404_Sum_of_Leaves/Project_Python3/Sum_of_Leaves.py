# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        sum = 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                sum += int(root.left.val)
            else:
                sum += self.sub_sumOfLeftLeaves(root.left)
        if root.right is not None:
            sum += self.sub_sumOfLeftLeaves(root.right)
        return sum
    
    def sub_sumOfLeftLeaves(self, node):
        sum = 0
        if node.left is not None:
            if node.left.left is None and node.left.right is None:
                sum = int(node.left.val)
            else:
                sum += self.sub_sumOfLeftLeaves(node.left)
        if node.right is not None:
            sum += self.sub_sumOfLeftLeaves(node.right)
        return sum

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

    result = sl.sumOfLeftLeaves(root)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
