# coding: utf-8

import sys
import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        fastPtr = head
        slowPtr = head
        while fastPtr != None and fastPtr.next != None:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            if fastPtr == slowPtr:
                return True

        return False


def set_node(data):
    node = ListNode(data[0])
    temp_node = node

    for i in range(1,len(data)):
        temp_node.next = ListNode(data[i])
        temp_node = temp_node.next
    
    return node


def output_node(node):
    if node == None:
        return ''
    tempStr = node.val
    temp_node = node.next
    while temp_node != None:
        tempStr += ',' + temp_node.val
        temp_node = temp_node.next
    return tempStr


def main():
    args = sys.argv
    argc = len(args)

    print("args[0] = %s %s" %(args[0], args[1]) )
    tempStr = args[1].rstrip()
    flds = tempStr.split(',')
    node = set_node(flds)

    print("node p = %s" %(output_node(node)))

    time0 = time.time()

    sl = Solution()
    print(sl.hasCycle(node))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
