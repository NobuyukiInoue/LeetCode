# coding: utf-8

import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    ope_l = OperateListNode()
    node = ope_l.createListNode(flds[0])
    print("node = {0}".format(ope_l.ListNodeToString(node)))

    n = int(flds[1])
    print("n = {0:d}".format(n))

    time0 = time.time()

    sl = Solution()
    result = sl.removeNthFromEnd(node, n)
    print("node = {0}".format(ope_l.ListNodeToString(result)))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
