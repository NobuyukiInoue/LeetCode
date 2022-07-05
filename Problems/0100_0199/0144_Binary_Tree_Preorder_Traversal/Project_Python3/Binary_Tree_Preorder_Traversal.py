# coding: utf-8

import os
import re
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def preorderTraversal(self, root: TreeNode) -> List[int]:
    def preorderTraversal(self, root):
        # 28ms
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node):
        if node is None:
            return
        self.res.append(node.val)
        if node.left is not None:
            self.helper(node.left)
        if node.right is not None:
            self.helper(node.right)
        return

    def preorderTraversal2(self, root):
        # 24ms
        res = []
        rights = []
        while root is not None:
            res.append(root.val)
            if root.right is not None:
                rights.append(root.right)
            root = root.left
            if root is None and len(rights) > 0:
                root = rights.pop()
        return res

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
    result = sl.preorderTraversal(root)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
