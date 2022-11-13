# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple, Optional

from Node.Node import Node
from Node.OperateNode import OperateNode

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 37ms - 43ms
        memo = {}
        def deepcopy(n):
            if not n:
                return
            if n in memo:
                return memo[n]
            memo[n] = new = Node( n.val )
            new.next   = deepcopy(n.next  )
            new.random = deepcopy(n.random)
            return new
        return deepcopy(head)

    def copyRandomList_normal(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 58ms - 121ms
        if head is None:
            return None

        def findNodeIndex(nodes: List[Node], target: Node) -> int:
            if target is None:
                return None
            for i, node in enumerate(nodes):
                if target == node:
                    return i
            return -1

        new_head = Node(head.val)
        old_cur, new_cur = head, new_head
        old_nodes, new_nodes = [], []
        while not old_cur is None:
            new_cur.val = old_cur.val
            old_nodes.append(old_cur)
            new_nodes.append(new_cur)
            if old_cur.next is not None:
                new_cur.next = Node(old_cur.next.val)
            old_cur, new_cur = old_cur.next, new_cur.next
        old_cur , new_cur = head, new_head
        while not new_cur is None:
            random = findNodeIndex(old_nodes, old_cur.random)
            if random is not None:
                new_cur.random = new_nodes[random]
            old_cur, new_cur = old_cur.next, new_cur.next
        return new_head

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
    str_args = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    ope_n = OperateNode()
    if flds[0] == "[]" or flds[0] == "":
        head = None
    else:
        head = ope_n.createNode(flds)
    print("head = {0}".format(ope_n.nodeToListListArray(head)))

    sl = Solution()
    time0 = time.time()

    result = sl.copyRandomList(head)

    time1 = time.time()

    print("result = {0}".format(ope_n.nodeToListListArray(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
