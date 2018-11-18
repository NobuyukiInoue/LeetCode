# coding: utf-8

import sys
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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


def set_node(data):
    if data == None:
        return
    new_node = TreeNode(data[0])
    if data[1] != "null":
        new_node.left = TreeNode(data[1])
    if data[2] != "null":
        new_node.right = TreeNode(data[2])
    return new_node


def output_node(node):
    tempStr = ""
    if node != None:
        tempStr += node.val + ","
    if node.left != None:
        tempStr += node.left.val + ","
    else:
        tempStr += "null,"
    if node.right != None:
        tempStr += node.right.val
    else:
        tempStr += "null"

    return tempStr


def main():
    args = sys.argv
    argc = len(args)

    print("args[0] = %s args[1] = %s" %(args[0], args[1]) )
    flds = args[1].rstrip().split(chr(0x09)) # remove LF and splip [TAB]
    print("flds[0] = %s fls[1] = %s" %(flds[0], flds[1]) )
    arg1 = flds[0].split(',')
    arg2 = flds[1].split(',')

    p = set_node(arg1)
    q = set_node(arg2)

    print("node p = %s" %(output_node(p)))
    print("node q = %s" %(output_node(q)))

    time0 = time.time()

    sl = Solution()
    print(sl.isSameTree(p, q))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
