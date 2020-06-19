# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#    def findTilt(self, root: TreeNode) -> int:
    def findTilt(self, root):
        ret = [0]
        self.helper(root, ret)
        return ret[0]

    def helper(self, node, ret):
        if node == None:
            return 0

        lSum = self.helper(node.left, ret)
        rSum = self.helper(node.right, ret)
        ret[0] += self.intAbs(lSum - rSum)
        return lSum + rSum + node.val

    def intAbs(self, x):
        if x >= 0:
            return x
        else:
            return -x

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds)
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()

    time0 = time.time()

    result = sl.findTilt(root)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
