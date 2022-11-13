from typing import List, Dict, Tuple

from .Node import Node

class OperateNode:
    def createNode(self, flds: List[str]) -> Node:
        nodes = []
        for fld in flds:
            nodes.append(Node(int(fld.split(",")[0]), None, None))
        head = nodes[0]
        cur = head
        i = 0
        while True:
            random = flds[i].split(",")[1]
            if random != "null":
                cur.random = nodes[int(random)]
            if i == len(nodes) - 1:
                break
            cur.next = nodes[i + 1]
            cur = cur.next
            i += 1
        return head

    def nodeToListListArray(self, head: Node) -> List[List[int]]:
        nodes, cur = [], head
        while not cur is None:
            nodes.append(cur)
            cur = cur.next
        flds, cur = [], head
        while not cur is None:
            flds.append([cur.val, self.findNodeIndex(nodes, cur.random)])
            cur = cur.next
        return flds

    def findNodeIndex(self, nodes: List[Node], target: Node) -> int:
        if target is None:
            return None
        for i, node in enumerate(nodes):
            if target == node:
                return i
        return -1
