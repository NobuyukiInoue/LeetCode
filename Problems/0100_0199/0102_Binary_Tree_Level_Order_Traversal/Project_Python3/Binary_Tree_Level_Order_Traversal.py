# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def levelOrder(self, root: TreeNode) -> List[List[int]]:
    def levelOrder(self, root):
        # 40ms
        resultList = []
        self.helper(root, resultList, 0)
        return resultList

    def helper(self, node, resultList, level):
        if node is None:
            return
        if len(resultList) < level + 1:
            resultList.append([])
        resultList[level].append(node.val)
        self.helper(node.left, resultList, level + 1)
        self.helper(node.right, resultList, level + 1)
        return

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

    sl = Solution()
    time0 = time.time()

    result = sl.levelOrder(root)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
