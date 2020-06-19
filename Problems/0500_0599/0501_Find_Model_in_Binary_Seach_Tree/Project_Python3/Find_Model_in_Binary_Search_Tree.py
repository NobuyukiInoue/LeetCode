import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

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
    print("%s" %flds)

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds)
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()

    time0 = time.time()

    result = sl.findMode(root)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
