import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def getMinimumDifference0(self, root):
        L = []
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(abs(a - b) for a, b in zip(L, L[1:]))

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.vals = []
        self.get_all_vals2(root)
        '''
        diff_min = sys.maxsize
        for i in range(len(self.vals)):
            for j in range(i + 1, len(self.vals)):
                temp = abs(self.vals[i] - self.vals[j])
                if temp < diff_min:
                    diff_min = temp
        return diff_min
        '''
        return min(abs(a - b) for a, b in zip(self.vals, self.vals[1:]))

    def get_all_vals2(self, node):
        if node == None:
            return
        self.vals.append(node.val)
        if node.left != None:
            self.get_all_vals2(node.left)
        if node.right != None:
            self.get_all_vals2(node.right)
        return

    def getMinimumDifference3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.vals_count = 0
        self.get_all_vals3_1(root)
        self.vals = [0]*self.vals_count
        self.vals_count = 0
        self.get_all_vals3_2(root)
        diff_min = sys.maxsize
        for i in range(len(self.vals)):
            for j in range(i + 1, len(self.vals)):
                temp = abs(self.vals[i] - self.vals[j])
                if temp < diff_min:
                    diff_min = temp
        return diff_min

    def get_all_vals3_1(self, node):
        if node == None:
            return
        self.vals_count += 1
        if node.left != None:
            self.get_all_vals3_1(node.left)
        if node.right != None:
            self.get_all_vals3_1(node.right)
        return

    def get_all_vals3_2(self, node):
        if node == None:
            return
        self.vals[self.vals_count] = node.val
        self.vals_count += 1
        if node.left != None:
            self.get_all_vals3_2(node.left)
        if node.right != None:
            self.get_all_vals3_2(node.right)
        return

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds)
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.getMinimumDifference(root)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
