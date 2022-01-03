from typing import List, Dict, Tuple
from .Node import Node

class OperateNode:
    def createNode(self, data: List[int]) -> Node:
        nodes = [None for n in range(len(data))]
        for i, _ in enumerate(data):
            nodes[i] = Node(i + 1, None)
        for i, _ in enumerate(nodes):
            nodes[i].neighbors = [nodes[col - 1] for col in data[i]]
        return nodes[0]

    def nodeToString(self, node: Node) -> str:
        if not node:
            return "[]"
        elif node.neighbors is None:
            return "[[]]"
        resultStr = ""
        data = {}
        data[node.val] = [nei.val for nei in node.neighbors]
        for nei in node.neighbors:
            data[nei.val] = [nei2.val for nei2 in nei.neighbors]
            for nei2 in nei.neighbors:
                if nei2.val not in data:
                    data[nei2.val] = [nei3.val for nei3 in nei2.neighbors]
        resultStr = ""
        for k in data.keys():
            if resultStr == "":
                resultStr += str(data[k])
            else:
                resultStr += "," + str(data[k])
        return resultStr
