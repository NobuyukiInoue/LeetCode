# coding: utf-8

import copy
import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    def pathSum(self, root, sum):
        # 52ms
        results = []
        self.dfs(root, sum, [], results)
        return results

    def dfs(self, root, sum, tmp, results):
        if not root:
            return
        if root.left is None and root.right is None and sum == root.val:
            results.append(tmp+[root.val])
            return
        self.dfs(root.left, sum-root.val, tmp+[root.val], results)
        self.dfs(root.right, sum-root.val, tmp+[root.val], results)

    def pathSum_work(self, root, sum):
        # 384ms
        self.results = []
        if root is None or root.val is None:
            return None
        arr = []
        total = 0
        self.helper(root, arr, total, sum)
        return self.results

    def helper(self, node, arr, total, sum):
        if node.val is None:
            return
        arr.append(node.val)
        total += node.val
        if node.left is None and node.right is None:
            if total == sum:
                self.results.append(arr)
                return
        if node.left is not None:
            self.helper(node.left, copy.deepcopy(arr), total, sum)
        if node.right is not None:
            self.helper(node.right, copy.deepcopy(arr), total, sum)
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds[0])
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sum = int(flds[1])
    print("sum = {0:d}".format(sum))

    sl = Solution()
    time0 = time.time()

    result = sl.pathSum(root, sum)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
