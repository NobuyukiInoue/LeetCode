# coding: utf-8

import os
import sys
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node is not None:
            if node.next is not None:
                prev_node = node
                node.val = node.next.val
                node = node.next
            else:
                break
        prev_node.next = None

def output_ListNode(node):
    if node == None:
        return

    resultStr = node.val

    work_node = node
    while work_node.next != None:
        resultStr += " -> " + str(work_node.next.val)
        work_node = work_node.next
    
    return resultStr

def set_node(flds):
    if len(flds) <= 0:
        return None

    node = ListNode(flds[0])
    work_node = node

    for i in range(1, len(flds)):
        work_node.next = ListNode(flds[i])
        work_node = work_node.next

    return node

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
    node = set_node(flds[0].split(","))

    print("node = %s" %(output_ListNode(node)))

    time0 = time.time()

    sl = Solution()
    sl.deleteNode(node)
    print("node = %s" %(output_ListNode(node)))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
