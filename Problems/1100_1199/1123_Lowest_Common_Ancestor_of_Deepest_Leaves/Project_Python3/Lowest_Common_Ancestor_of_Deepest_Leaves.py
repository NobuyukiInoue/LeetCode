# coding: utf-8

import os
import sys
import time
from typing import Optional, List, Dict, Tuple

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 41ms - 52ms
        def get_deepest_node(node: Optional[TreeNode], depth) -> (int, TreeNode):
            if node is None:
                return (0, None)
            (l_depth, l_node) = get_deepest_node(node.left, depth + 1)
            (r_depth, r_node) = get_deepest_node(node.right, depth + 1)
            if l_depth > r_depth:
                return (l_depth + 1, l_node)
            if l_depth < r_depth:
                return (r_depth + 1, r_node)
            return (l_depth + 1, node)
        (_max_depth, ans) = get_deepest_node(root, 0)
        return ans

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
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds.split(","))
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.lcaDeepestLeaves(root)

    time1 = time.time()

    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
