# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class BSTIterator:
    # 72ms

#   def __init__(self, root: TreeNode):
    def __init__(self, root):
        self.nums = []
        def dfs(node):
            if node == None:
                return
            if node.left != None:
                dfs(node.left)
            self.nums.append(node.val)
            if node.right != None:
                dfs(node.right)

        dfs(root)
        self.index = 0

#   def next(self) -> int:
    def next(self):
        """
        @return the next smallest number
        """
        if self.index < len(self.nums):
            self.index += 1
            return self.nums[self.index - 1]

#   def hasNext(self) -> bool:
    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.nums)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class Solution:
    def main(self, cmds, mynode):
        for cmd in cmds:
            if cmd == "BSTIterator":
                BI = BSTIterator(mynode)
                print("BSTIterator iterator = new BSTIterator(root);")
            elif cmd == "next" and BI != None:
                print("iterator.next();\t ... {0:d}".format(BI.next()))
            elif cmd == "hasNext" and BI != None:
                print("iterator.hasNext();\t ... {0}".format(BI.hasNext()))

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
    flds = temp.replace("\"","").replace(", ",",").rstrip().split("],[[[")
    cmds = flds[0].replace("[[", "").split(",")

    node_flds = (flds[1].split("]],["))[0]
    ope_t = OperateTreeNode()

    if len(node_flds) > 0:
        mynode = ope_t.createTreeNode(node_flds)
    else:
        mynode = None

    print("mynode = \n[{0}]".format(ope_t.treeToStaircaseString(mynode)))

    sl = Solution()
    time0 = time.time()

    sl.main(cmds, mynode)

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
