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
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        self.max_mode = 1
        self.cur_mode = 1
        self.max_modes = set([root.val])
        self.prev_node = None

        self.find_mode_inorder(root)

        return list(self.max_modes)
        
    def find_mode_inorder(self, root):
        if root is None:
            return

        self.find_mode_inorder(root.left)

        self.update_modes(root)
        self.prev_node = root

        self.find_mode_inorder(root.right)

    def update_modes(self, root):
        if self.prev_node is not None and self.prev_node.val == root.val:
            self.cur_mode += 1
            if self.cur_mode >= self.max_mode:
                if self.cur_mode > self.max_mode:
                    self.max_modes.clear()
                self.max_modes.add(root.val)
                self.max_mode = self.cur_mode
        else:
            self.cur_mode = 1
            if self.max_mode == self.cur_mode:
                self.max_modes.add(root.val)

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
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("%s" %flds)

    root = set_node(flds, 0, 0)
    ol = output_TreeNode()
    print("%s" %ol.output(root))

    sl = Solution()

    time0 = time.time()

    result = sl.findMode(root)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
