import os
import sys
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class output_TreeNode:
    def __init__(self):
        self.resultStr = []

    def output(self, node):
        self.output_TreeNode(node, 0)
        return self.print_resultStr()

    def output_TreeNode(self, node, n):
        if node == None:
            return
        if len(self.resultStr) <= n:
            self.resultStr.append("(" + str(node.val) + ")")
        else:
            self.resultStr[n] += ",(" + str(node.val) + ")"
        if node.left != None:
            self.output_TreeNode(node.left, n + 1)
        if node.right != None:
            self.output_TreeNode(node.right, n + 1)
        return

    def print_resultStr(self):
        outputStr = ""
        for i in range(len(self.resultStr)):
            outputStr += self.resultStr[i] + "\n"
        return outputStr

def set_node(flds, depth, pos):
    if len(flds) <= 0:
        return None

    cur_pos = 0
    for i in range(depth):
        cur_pos += 2 ** i
    
    if cur_pos + pos > len(flds) - 1:
        return None

    if flds[cur_pos + pos] == 'null':
        return None

    node = TreeNode(int(flds[cur_pos + pos]))
    node.left = set_node(flds, depth + 1, 2*pos)
    node.right = set_node(flds, depth + 1, 2*pos + 1)

    return node

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    root = set_node(flds, 0, 0)

    time0 = time.time()

    sl = Solution()
    result = sl.getMinimumDifference(root)

    print("result = %d" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
