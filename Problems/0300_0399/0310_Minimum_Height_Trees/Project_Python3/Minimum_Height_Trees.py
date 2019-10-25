# coding: utf-8

import collections
import os
import sys
import time
import heapq

class Solution:
#   def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    def findMinHeightTrees(self, n, edges):
        # 268ms
        if not edges:
            if n == 1:
                return [0]
            else:
                return []
        table, wlist = [set() for i in range(n)], collections.deque()
        for e in edges:
            table[e[0]].add(e[1])
            table[e[1]].add(e[0])
        for i in range(n):
            if len(table[i]) == 1:
                wlist.append(i)
        steps = 0
        node1, node2 = n, n
        while wlist:
            steps += 1
            len_level = len(wlist)
            if len_level == 1:
                return list(wlist)
            for i in range(len_level):
                prev_node1 = node1
                node1 = wlist.popleft()
                if node1 == node2:
                    return [node1,prev_node1]
                node2 = table[node1].pop() 
                table[node2].remove(node1)
                if (len(table[node2]) == 1):
                    wlist.append(node2)
        return  list(wlist)

    def findMinHeightTrees2(self, n, edges):
        # 284ms
        if n == 1:
            return [0]
        neighbors = collections.defaultdict(list)
        degrees = collections.defaultdict(int)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        # First find the leaves
        preLevel, unvisited = [], set(range(n))
        for i in range(n):
            if degrees[i] == 1: preLevel.append(i)
            
        while len(unvisited) > 2:
            thisLevel = []
            for u in preLevel:
                unvisited.remove(u)
                for v in neighbors[u]:
                    if v in unvisited:
                        degrees[v] -= 1
                        if degrees[v] == 1:
                            thisLevel += [v]
            preLevel = thisLevel

        return preLevel

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
    flds = temp.replace(" ", "").replace("\"", "").split("],[[")

    n = int(flds[0].replace("[", ""))
    print("n = {0:d}".format(n))

    flds[1] = flds[1].replace("]]]", "")
    if len(flds[1]) > 0:
        dataStr = flds[1].split("],[")
        edges = [[int(n) for n in data.split(",") ] for data in dataStr]
    else:
        edges = [[]]

    print("edges = [")
    for i in range(len(edges)):
        if i == 0:
            print(" {0}".format(edges[i]))
        else:
            print(",{0}".format(edges[i]))
    print("]")

    time0 = time.time()

    sl = Solution()
    result = sl.findMinHeightTrees(n, edges)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
