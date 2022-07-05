# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Optional, Tuple

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # 216ms
        ans = []
        if n % 2 == 0: 
            return ans
        if n == 1:
            ans.append(TreeNode(0))
            return ans
        for i in range(1, n, 2):
            Ll = self.allPossibleFBT(i)
            Lr = self.allPossibleFBT(n - 1 - i)
            for node_l in Ll:
                for node_r in Lr:
                    node = TreeNode(0)
                    node.left = node_l
                    node.right = node_r
                    ans.append(node)
        return ans

    def allPossibleFBT2(self, n: int) -> List[Optional[TreeNode]]:
        # 180ms
        dp = dict()
        dp[1] = [TreeNode()]
        def helper(var_n: int) -> List[Optional[TreeNode]]:
            if var_n in dp:
                return dp[var_n]
            result = []
            for i in range(1, var_n - 2 + 1):
                left_trees = helper(i)
                right_trees = helper(var_n - i - 1)
                for tree_l in left_trees:
                    for tree_r in right_trees:
                        root = TreeNode()
                        root.left = tree_l
                        root.right = tree_r
                        result.append(root)
            dp[var_n] = result
            return result
        return helper(n)

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
    flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").rstrip()
    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.allPossibleFBT(n)

    time1 = time.time()

    cd = Codec()
    print("result = [")
    for i, node in enumerate(result):
        if i == 0:
            print(" [{0}]".format(cd.serialize(node)))
        else:
            print(",[{0}]".format(cd.serialize(node)))
    print("]")

    ope_t = OperateTreeNode()
    for i, node in enumerate(result):
        print("result[{0:d}] = \n{1}".format(i, ope_t.treeToStaircaseString(node)))
    print()
    for i, node in enumerate(result):
        print("result[{0:d}] = {1}".format(i, ope_t.tree2str(node)))
    print()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
