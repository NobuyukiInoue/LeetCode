# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds[0])
    p = ope_t.createTreeNode(flds[1])
    q = ope_t.createTreeNode(flds[2])

    print("root = \n{0}".format((ope_t.treeToStaircaseString(root))))
    print("root = {0}\n".format(ope_t.tree2str(root)))
    print("p = \n{0}".format((ope_t.treeToStaircaseString(p))))
    print("p = {0}\n".format(ope_t.tree2str(p)))
    print("q = \n{0}".format((ope_t.treeToStaircaseString(q))))
    print("q = {0}\n".format(ope_t.tree2str(q)))

    sl = Solution()
    time0 = time.time()

    result = sl.lowestCommonAncestor(root, p, q)

    time1 = time.time()

    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
