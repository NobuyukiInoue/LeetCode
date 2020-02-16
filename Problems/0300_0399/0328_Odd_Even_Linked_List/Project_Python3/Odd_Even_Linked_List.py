import os
import sys
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
#   def oddEvenList(self, head: ListNode) -> ListNode:
    def oddEvenList2(self, head):
        # 40ms
        if not head or not head.next:
            return head

        next_head = head.next
        cursor = head
        count = 1
        last_odd_node = None

        while cursor:
            if count % 2 == 1:
                last_odd_node = cursor
            temp_next = cursor.next
            if cursor.next:
                cursor.next = cursor.next.next
            cursor = temp_next
            count += 1

        last_odd_node.next = next_head

        return head

    def oddEvenList2(self, head):
        # 48ms
        if head == None:
            return None
        count = 0
        list_odd, list_even = [], []
        while head != None:
            if count % 2 == 0:
                list_even.append(head.val)
            else:
                list_odd.append(head.val)
            count += 1
            head = head.next

        if len(list_even) > 0:
            res = ListNode(list_even[0])
            res_head = res
            for i in range(1, len(list_even)):
                res.next = ListNode(list_even[i])
                res = res.next

            if len(list_odd) > 0:
                res.next = ListNode(list_odd[0])
                res = res.next
                for i in range(1, len(list_odd)):
                    res.next = ListNode(list_odd[i])
                    res = res.next

        return res_head


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

    if len(flds) == 0:
        head = None
        print("head = []")
    else:
        nums = [int(val) for val in flds.split(",")]
        print("nums = %s " %nums)

        head = set_nodes(nums, 0)
        print("head = %s " %output_nodes(head))

    time0 = time.time()

    sl = Solution()
    result = sl.oddEvenList(head)

    time1 = time.time()

    if result != None:
        print("result = %s" %output_nodes(result))
    else:
        print("result = []")

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
