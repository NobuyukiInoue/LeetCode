# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def generateTrees(self, n: int) -> List[TreeNode]:
    def generateTrees(self, n: int) -> [TreeNode]:
        # 60ms
        def generate(left: int, right: int):
            if right - left < 0:
                return [None]
            elif right - left == 0:
                return [TreeNode(left)]
            else:
                res = []
                for curr in range(left, right + 1):
                    leftChild = generate(left, curr - 1)
                    rightChild = generate(curr + 1, right)
                    for l in leftChild:
                        for r in rightChild:
                            root = TreeNode(curr)
                            root.left = l
                            root.right = r
                            res.append(root)
                return res
        if n == 0:
            return []
        return generate(1, n)

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
    n = int(temp.replace("[","").replace("]","").rstrip())
    print("num = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.generateTrees(n)

    time1 = time.time()

    ope_t = OperateTreeNode()
    for i, res in enumerate(result):
        print("result[{0:d}] = \n{1}".format(i, ope_t.treeToStaircaseString(result[i])))
        print("result[{0:d}] = {1}".format(i, ope_t.tree2str(result[i])))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
