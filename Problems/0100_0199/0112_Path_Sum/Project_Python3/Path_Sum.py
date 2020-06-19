# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            else:
                return False

        if root.left != None:
            if self.hasPathSum(root.left, sum - root.val):
                return True

        if root.right != None:
            if self.hasPathSum(root.right, sum - root.val):
                return True

        return False

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds[0])
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))
    sum = int(flds[1])
    print("sum = {0:d}".format(sum))

    sl = Solution()
    time0 = time.time()

    result = sl.hasPathSum(root, sum)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
