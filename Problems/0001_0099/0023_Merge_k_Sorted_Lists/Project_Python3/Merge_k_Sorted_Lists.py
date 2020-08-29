import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        ans = []
        ope_l = OperateListNode()
        for ln in lists:
            while ln:
                ans.append(ln.val)
                ln = ln.next
        ans.sort()
        result = ope_l.createSubListNode(ans, 0)

        return result

    def mergeKLists_work(self, lists: 'List[ListNode]') -> 'ListNode':
        if len(lists) < 1:
            return None
        if lists is None:
            return None

        none_count = 0
        for temp_list in lists:
            if temp_list is None:
                none_count += 1
        if none_count == len(lists):
            return None

        current_lists = lists
        work_list = None
        while True:
            current_min = sys.maxsize
            end_count = 0
            for i in range(len(current_lists)):
                if current_lists[i] is None:
                    end_count += 1
                    continue
                if current_lists[i].val < current_min:
                    current_index = i
                    current_min = current_lists[i].val
            if end_count == len(current_lists):
                break

            if work_list is None:
                root = ListNode(current_min)
                work_list = root
            else:
                work_list.next = ListNode(current_min)
                work_list = work_list.next

            current_lists[current_index] = current_lists[current_index].next

        return root

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    lists = []
    ope_l = OperateListNode()
    if len(flds) >= 1 and flds[0] != "":
        for i in range(len(flds)):
            lists.append(ope_l.createListNode(flds[i]))
            print("lists[{0:d}] = {1} ".format(i, ope_l.ListNodeToString(lists[i])))
    else:
        lists = [None]

    sl = Solution()
    time0 = time.time()

    result = sl.mergeKLists(lists)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
