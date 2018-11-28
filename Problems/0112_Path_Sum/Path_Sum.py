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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            else:
                return False

        if root.left != None:
            if self.hasPathSum(root.left, sum - root.val):
                return True

        if root.right != None:
            if self.hasPathSum(root.right, sum - root.val):
                return True

        return False


def load_sample0_treeData():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    return root

def load_sample2_treeData():
    root = TreeNode(1)
    root.left = TreeNode(2)
    return root


def main():
    time0 = time.time()

    sl = Solution()
    '''
    root = load_sample0_treeData()
    print(sl.hasPathSum(root, 22))
    '''
    root = load_sample2_treeData()
    print(sl.hasPathSum(root, 1))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
