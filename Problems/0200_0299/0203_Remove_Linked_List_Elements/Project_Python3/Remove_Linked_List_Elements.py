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

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

def set_nodes(nums, index):
    if nums == None:
        return None

    if index >= len(nums):
        return None
    
    node = ListNode(nums[index])
    node.next = set_nodes(nums, index + 1)

    return node

def output_nodes(node):
    if node == None:
        return ""
    retStr = str(node.val) 

    if node.next != None:
        retStr += " -> " + output_nodes(node.next)
    return retStr

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
    str_args = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()
    flds = str_args.split("],[")

    nums = str_to_int_array(flds[0])
    val = int(flds[1])
    print("nums1 = %s " %nums)
    print("val = %d" %val)

    head = set_nodes(nums, 0)
    print("nodes = %s " %output_nodes(head))

    time0 = time.time()

    sl = Solution()
    result = sl.removeElements(head, val)

    time1 = time.time()

    print("result = %s" %output_nodes(result))
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
