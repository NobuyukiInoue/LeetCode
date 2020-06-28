# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s.val == t.val:
            if self.isSameTree(s, t):
                return True
        if s.left != None:
            if self.isSubtree(s.left, t):
                return True
        if s.right != None:
            if self.isSubtree(s.right, t):
                return True
        return False        

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None) and (q == None):
            return True
        elif (p == None) or (q == None):
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

    s = ope_t.createTreeNode(flds[0])
    print("s = \n{0}".format(ope_t.treeToStaircaseString(s)))
    print("s = {0}".format(ope_t.tree2str(s)))

    t = ope_t.createTreeNode(flds[1])
    print("t = \n{0}".format(ope_t.treeToStaircaseString(t)))
    print("t = {0}".format(ope_t.tree2str(t)))

    sl = Solution()
    time0 = time.time()
    result = sl.isSubtree(s, t)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
