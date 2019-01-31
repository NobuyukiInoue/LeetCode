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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # first get the len of the linked list
        len = 0
        p = head
        while p is not None:
            p = p.next
            len += 1
        
        # special case: if the head needs to be removed, i.e. when len == n
        if len == n:
            return head.next
        
        # otherwise, go to the node before the one needs to be deleted
        p = head
        i = 0
        while i < len-n-1:
            p = p.next
            i += 1
        
        # remove the Nth node from end of list
        p.next = p.next.next

        return head

    def removeNthFromEnd_work(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head

        if head == None:
            return None

        depth, head = self.get_depth(head, 0, n)
        return head

    def get_depth(self, node, current_depth, n):
        if node == None:
            return current_depth, node
        else:
            depth_max, node.next = self.get_depth(node.next, current_depth + 1, n)
            if current_depth == depth_max - n:
                if n == 1:
                    node = None
                else:
                    node = node.next
            return depth_max, node

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    node = set_node(flds[0].split(","))
    n = int(flds[1])

    print("node = %s" %(output_ListNode(node)))
    print("n = %d" %n)

    time0 = time.time()

    sl = Solution()
    result = sl.removeNthFromEnd(node, n)
    print("node = %s" %(output_ListNode(result)))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()