import os
import sys
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if head is None or k < 2:
            return head
        
        next_head = head
        for i in range(k - 1):
            next_head = next_head.next
            if next_head is None:
                return head
        ret = next_head
        
        current = head
        while next_head:
            tail = current
            prev = None
            for i in range(k):
                if next_head:
                    next_head = next_head.next
                _next = current.next
                current.next = prev
                prev = current
                current = _next
            tail.next = next_head or current
                
        return ret

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

def set_nodes(nums, index):
    if index >= len(nums):
        return None
    
    node = ListNode(nums[index])
    node.next = set_nodes(nums, index + 1)

    return node

def output_nodes(ll):
    retStr = str(ll.val) 

    if ll.next != None:
        retStr += " -> " + output_nodes(ll.next)
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    num1 = str_to_int_array(flds[0])
    k = int(flds[1])
    print("nums1 = %s " %num1)

    head = set_nodes(num1, 0)
    print("head = %s, k = %d" %(output_nodes(head), k))

    time0 = time.time()

    sl = Solution()
    result = sl.reverseKGroup(head, k)

    print("result = %s" %output_nodes(result))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
