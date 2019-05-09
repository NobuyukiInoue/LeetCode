import os
import sys
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        ans = []
        for ln in lists:
            while ln:
                ans.append(ln.val)
                ln = ln.next
        ans.sort()
        result = set_nodes(ans, 0)

        return result

    def mergeKLists_work(self, lists: 'List[ListNode]') -> 'ListNode':
        if len(lists) < 1:
            return None
        if lists == None:
            return None

        none_count = 0
        for temp_list in lists:
            if temp_list == None:
                none_count += 1
        if none_count == len(lists):
            return None

        current_lists = lists
        work_list = None
        while True:
            current_min = sys.maxsize
            end_count = 0
            for i in range(len(current_lists)):
                if current_lists[i] == None:
                    end_count += 1
                    continue
                if current_lists[i].val < current_min:
                    current_index = i
                    current_min = current_lists[i].val
            if end_count == len(current_lists):
                break

            if work_list == None:
                root = ListNode(current_min)
                work_list = root
            else:
                work_list.next = ListNode(current_min)
                work_list = work_list.next

            current_lists[current_index] = current_lists[current_index].next

        return root

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

def output_nodes(ll):
    if ll == None:
        return ""

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

    nums = [0]*len(flds)
    for i in range(len(flds)):
        nums[i] = str_to_int_array(flds[i])
        print("nums[%d] = %s " %(i, nums[i]))

    lists = []
    for i in range(len(nums)):
        lists.append(set_nodes(nums[i], 0))
        print("lists[%d] = %s " %(i, output_nodes(lists[i])))

    time0 = time.time()

    sl = Solution()
    result = sl.mergeKLists(lists)

    time1 = time.time()
    print("result = %s" %output_nodes(result))
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
