# coding: utf-8

import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

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


def loop_main(temp):
    flds = temp.replace("[","").replace("]","").rstrip()

    ope_l = OperateListNode()
    node = ope_l.createListNode(flds)
    print("node = {0}".format(ope_l.ListNodeToString(node)))

    sl = Solution()
    time0 = time.time()

    result_node = sl.reverseList(node)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result_node)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))


if __name__ == "__main__":
    main()
