import os
import sys
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
#   def rotateRight(self, head: ListNode, k: int) -> ListNode:
    def rotateRight(self, head, k):
        # 24ms
        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy

        i = 0
        while fast.next != None:
            fast = fast.next
            i += 1

        j = i - k%i
        while j > 0:
            slow = slow.next
            j -= 1

        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next   

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(val) for val in flds[0].split(",")]
    print("nums = {0}".format(nums))

    head = set_nodes(nums, 0)
    k = int(flds[1])
    print("head = {0}, k = {1:d}".format(output_nodes(head), k))

    time0 = time.time()

    sl = Solution()
    result = sl.rotateRight(head, k)

    time1 = time.time()

    print("result = {0}".format(output_nodes(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
