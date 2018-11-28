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
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        curr = dummy
        while head:
            if head.val != val:
                curr.next = head
                curr = curr.next
                head = head.next
            else:
                head = head.next
        curr.next = None
        return dummy.next


    def removeElements_work(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp_node = head
        while temp_node != None:
            if temp_node.next != None:
                if temp_node.next.val == val:
                    temp_node.next = temp_node.next.next
            temp_node = temp_node.next
        return head


def set_node(data):
    if len(data) == 0:
        return None
    node = ListNode(data[0])
    temp_node = node

    for i in range(1,len(data)):
        temp_node.next = ListNode(data[i])
        temp_node = temp_node.next
    
    return node


def output_node(node):
    if node == None:
        return ''
    tempStr = str(node.val)
    temp_node = node.next
    while temp_node != None:
        tempStr += ',' + str(temp_node.val)
        temp_node = temp_node.next
    return tempStr


def array_str_to_int(numbersStr):
    if len(numbersStr) == 0:
        return ""
    if numbersStr[0] == '':
        return ""
    numbers = [0]*len(numbersStr)
    for i in range(len(numbersStr)):
        numbers[i] = int(numbersStr[i])
    return numbers


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


def loop_main(temp):
    flds = temp.split(", ")
    numsStr = flds[0].replace("[","").replace("]","").split(",")
    nums = array_str_to_int(numsStr)
    val = int(flds[1])

    head = set_node(nums)
    print("nodes = %s" %(output_node(head)))

    time0 = time.time()

    sl = Solution()
    result = sl.removeElements(head, val)
    print("result = %s" %(output_node(result)))

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
