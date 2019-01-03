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
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target-root.val) + self.find_paths(root.right, target-root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0

    def __init__(self):
        self.resultStr = []

    def pathSum_work(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        if root.val >= sum:
            total = 0
        else:
            total = root.val
        self.HitSumCount = 0
        self.nextSum(root.left, sum, total)
        self.nextSum(root.right, sum, total)
        return self.HitSumCount

    def nextSum(self, node, sum, total):
        if node == None:
            return
        if node.val != 'null':
            if total + node.val == sum:
                self.HitSumCount += 1
                total = 0
            elif total + node.val < sum:
                total += node.val
            else:
                total = 0
        else:
            total = 0
        if node.left != None:
            self.nextSum(node.left, sum, total)
        if node.right != None:
            self.nextSum(node.right, sum, total)
        return

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
        for i in range(len(self.resultStr)):
            print(self.resultStr[i])

def set_node(flds, depth, pos):
    if len(flds) <= 0:
        return None

    cur_pos = 0
    for i in range(depth):
        cur_pos += 2 ** i
    
    if cur_pos + pos > len(flds) - 1:
        return None

    if flds[cur_pos + pos] == 'null':
        node = TreeNode(flds[cur_pos + pos])
    else:
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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    var_str = temp.replace("\"","").rstrip()
    print("%s" %var_str)
    flds = var_str.split("],")
    root_str = flds[0].replace("root = ", "").replace("[", "").split(",")

    root = set_node(root_str, 0, 0)
    sl = Solution()
    sl.output_TreeNode(root, 0)
    sl.print_resultStr()

    sum = int(flds[1].replace("sum = ", ""))
    print("s = %d" %sum)

    time0 = time.time()

    result = sl.pathSum(root, sum)

    print("result = %d" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
