# coding: utf-8

from collections import deque
import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        ans=[[root.val]]
        queue=deque([root])
        while queue:
            cur_val_list=[]
            for i in range(len(queue)):
                root=queue.popleft()
                if root.left:
                    cur_val_list.append(root.left.val)
                    queue.append(root.left)
                if root.right:
                    cur_val_list.append(root.right.val)
                    queue.append(root.right)
            if cur_val_list:
                ans.insert(0,cur_val_list)
        return ans

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
    if len(flds) > 0:
        root = ope_t.createTreeNode(flds)
    else:
        root = None

    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.levelOrderBottom(root)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
