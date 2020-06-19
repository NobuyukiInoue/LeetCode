# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans

    def mergeTrees_work(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None:
            return None
        elif t1 != None and t2 != None:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
        elif t1 != None:
            node = TreeNode(t1.val)
            node.left = self.mergeTrees(t1.left, None)
            node.right = self.mergeTrees(t1.right, None)
        elif t2 != None:
            node = TreeNode(t2.val)
            node.left = self.mergeTrees(None, t2.left)
            node.right = self.mergeTrees(None, t2.right)

        return node

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None) and (q == None):
            return True
        elif (p == None) or (q == None):
            return False
        if p.val == q.val:
            if self.isSameTree(p.left, q.left):
                return self.isSameTree(p.right, q.right)
            else:
                return False
        else:
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    ope_t = OperateTreeNode()
    t1 = ope_t.createTreeNode(flds[0])
    t2 = ope_t.createTreeNode(flds[1])
    print("t1 = \n{0}".format(ope_t.treeToStaircaseString(t1)))
    print("t1 = {0}".format(ope_t.tree2str(t1)))
    print("t2 = \n{0}".format(ope_t.treeToStaircaseString(t2)))
    print("t2 = {0}".format(ope_t.tree2str(t2)))

    sl = Solution()
    time0 = time.time()

    result = sl.mergeTrees(t1, t2)

    time1 = time.time()

    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
