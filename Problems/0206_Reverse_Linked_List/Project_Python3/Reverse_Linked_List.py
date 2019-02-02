# coding: utf-8

import os
import sys
import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        node_list = []
        temp_node = head
        node_list.append(head.val)

        while temp_node.next != None:
            temp_node = temp_node.next
            node_list.append(temp_node.val)
        
        result_top = ListNode(node_list[len(node_list) - 1])
        temp_node = result_top

        for i in range(len(node_list) - 2, -1, -1):
            temp_node.next = ListNode(node_list[i])
            temp_node = temp_node.next
        
        return result_top


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


def loop_main(temp):
    tempStr = temp.replace("[","").replace("]","").rstrip()
    flds = tempStr.split(',')
    node = set_node(flds)

    print("node = %s" %(output_node(node)))

    time0 = time.time()

    sl = Solution()
    result_node = sl.reverseList(node)

    print("result = %s" %(output_node(result_node)))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
