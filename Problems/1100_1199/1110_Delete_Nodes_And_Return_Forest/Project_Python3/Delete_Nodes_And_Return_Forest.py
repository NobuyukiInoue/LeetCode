# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # 64ms
        to_delete_set = set(to_delete)
        res = []
        def helper(root, is_root):
            if not root:
                return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        helper(root, True)
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds[0].split(","))
    to_delete = [int(n) for n in flds[1].split(",")]

    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))
    print("to_detele = {0}\n".format(to_delete))

    sl = Solution()
    time0 = time.time()

    result = sl.delNodes(root, to_delete)

    time1 = time.time()

    cd = Codec()
    for i, node in enumerate(result):
        if i == 0:
            print("result = [[{0}]".format(cd.serialize(node)), end="")
        else:
            print(",[{0}]".format(cd.serialize(node)), end="")
    print("]\n")

    for i, node in enumerate(result):
        print("result[{0:d}] = \n{1}".format(i, ope_t.treeToStaircaseString(node)))
    print()
    for i, node in enumerate(result):
        print("result[{0:d}] = {1}".format(i, ope_t.tree2str(node)))
    print()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
