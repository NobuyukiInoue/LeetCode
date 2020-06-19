# coding: utf-8

import os
import re
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 96ms
        self.res = -sys.maxsize - 1
        self.oneSideSum(root)
        return self.res

    def oneSideSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = max(0, self.oneSideSum(root.left))
        r = max(0, self.oneSideSum(root.right))
        self.res = max(self.res, root.val + l + r)
        return root.val + max(l, r)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    temp = re.sub('#.*', "", temp)
    temp = re.sub('//.*', "", temp)
    if len(temp) == 0:
        return
        
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds)
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.maxPathSum(root)

    time1 = time.time()
    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
