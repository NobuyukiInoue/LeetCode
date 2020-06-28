# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def sumRootToLeaf(self, root: TreeNode) -> int:
    def sumRootToLeaf(self, root):
        # 36ms-44ms
        if not root:
            return 0

        def sub_sumRootToLeaf(root, val):
            val = val*2 + root.val
            if root.left == root.right:
                return val
            l, r = 0, 0
            if root.left != None:
                l = sub_sumRootToLeaf(root.left, val)
            if root.right != None:
                r = sub_sumRootToLeaf(root.right, val)
            return l + r

        return sub_sumRootToLeaf(root, 0)

    def sub_sumRootToLeaf2(self, root):
        # 44-60ms
        if not root:
            return []

        def sumRootToLeafSub(node, route):
            if node == None:
                self.result.append([route])
                return
            route.append(node.val)
            if node.left == None and node.right == None:
                self.result.append(route)
                return
            if node.left != None:
                sumRootToLeafSub(node.left, route[:])
            if node.right != None:
                sumRootToLeafSub(node.right, route[:])
            return

        route = []
        self.result = []
        sumRootToLeafSub(root, route)

        total = 0
        for tmp in self.result:
            subtotal = 0
            for i in range(len(tmp)):
                subtotal = subtotal*2 + tmp[i]
            total += subtotal
        return total

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

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds)
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.sumRootToLeaf(root)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
