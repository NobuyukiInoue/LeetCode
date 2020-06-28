# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    def rangeSumBST(self, root, L, R):
        # 224ms
        if root == None:
            return 0
        sum = root.val if root.val >= L and root.val <= R else 0
        if root.val <= R:
            sum += self.rangeSumBST(root.right, L, R)
        if root.val >= L:
            sum += self.rangeSumBST(root.left, L, R)
        return sum

    def rangeSumBST2(self, root, L, R):
        # 304ms
        if not root: return 0
        l = self.rangeSumBST(root.left, L, R)
        r = self.rangeSumBST(root.right, L, R)
        return l + r + (L <= root.val <= R) * root.val

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
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    L = int(flds[1])
    R = int(flds[2])
    print("L = {0:d}, R = {1:d}".format(L, R))

    sl = Solution()
    time0 = time.time()

    result = sl.rangeSumBST(root, L, R)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
