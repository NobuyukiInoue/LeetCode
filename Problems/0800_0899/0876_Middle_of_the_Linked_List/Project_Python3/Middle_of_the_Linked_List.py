import os
import sys
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
#   def middleNode(self, head: ListNode) -> ListNode:
    def middleNode(self, head):
        if not head.next:
            return head
        ar, depth = [], 1
        while head.next:
            head = head.next
            depth += 1
            ar.append(head)
        ar.append(head)
        return ar[depth//2 - 1]

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

    nums = [int(val) for val in flds.split(",")]
    print("nums = %s " %nums)

    head = set_nodes(nums, 0)
    print("head = %s " %output_nodes(head))

    time0 = time.time()

    sl = Solution()
    result = sl.middleNode(head)

    time1 = time.time()

    print("result = %s" %output_nodes(result))
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
