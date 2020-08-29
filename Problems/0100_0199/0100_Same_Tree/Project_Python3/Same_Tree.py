# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None) and (q is None):
            return True
        elif (p is None) or (q is None):
            return False
        if p.val == q.val:
            if self.isSameTree(p.left, q.left):
                return self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    ope_t = OperateTreeNode()
    p = ope_t.createTreeNode(flds[0])
    q = ope_t.createTreeNode(flds[1])

    print("p = \n{0}".format(ope_t.treeToStaircaseString(p)))
    print("p = {0}".format(ope_t.tree2str(p)))
    print("q = \n{0}".format(ope_t.treeToStaircaseString(q)))
    print("q = {0}".format(ope_t.tree2str(q)))

    sl = Solution()
    time0 = time.time()

    result = sl.isSameTree(p, q)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
