# coding: utf-8

import os
import re
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 120ms
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes2(self, root: TreeNode) -> int:
        # 84ms
        res = 0
        hight_l, height_r = None, None
        while root:
            if hight_l:
                hight_l = hight_l - 1
                height_r = self.getTreeHeight(root.right)
            else:
                hight_l, height_r = self.getTreeHeight(root.left), self.getTreeHeight(root.right)
            res += 1 << height_r
            if hight_l == height_r:
                root = root.right
            else:
                root = root.left
        return res
        
    def getTreeHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

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
    temp = re.sub('#.*', "", temp)
    temp = re.sub('//.*', "", temp)
    if len(temp) == 0:
        return
        
    flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").rstrip()

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds.split(","))
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.countNodes(root)

    time1 = time.time()
    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
