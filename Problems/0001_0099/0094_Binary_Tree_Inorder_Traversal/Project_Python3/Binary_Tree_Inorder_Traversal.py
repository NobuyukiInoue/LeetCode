# coding: utf-8

import os
import re
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def inorderTraversal(self, root: TreeNode) -> List[int]:
    def inorderTraversal(self, root):
        # 36ms
        self.res = []
        if root == None:
            return self.res
        self.helper(root)
        return self.res

    def helper(self, node):
        if node == None:
            return
        self.helper(node.left)
        self.res.append(node.val)
        self.helper(node.right)
        return

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

    result = sl.inorderTraversal(root)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
