# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    def findSmallestSetOfVertices(self, n, edges):
        # 1140ms
        visited = [False for i in range(n)]
        for i in edges:
            visited[i[1]] = True

        ans = []
        for j in range(len(visited)):
            if not visited[j]:
                ans.append(j)
        return ans

    def findSmallestSetOfVertices2(self, n, edges):
        # 1160ms
        return list(set(range(n)) - set(j for i, j in edges))

    def findSmallestSetOfVertices3(self, n, edges):
        # 1156ms
        source_nodes=set(range(n))
        for n1, n2 in edges:
            if n2 in source_nodes:
                source_nodes.remove(n2)
        return source_nodes

    def findSmallestSetOfVertices4(self, n, edges):
        # Time Limite Exceeded.
        list1 = []
        list2 = []
        for val1, val2 in edges:
            if val1 not in list1:
                list1.append(val1)
            if val2 not in list2:
                list2.append(val2)
        res = []
        for num in list1:
            if num not in list2 and num not in res:
                res.append(num)
        return res

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
    flds = temp.replace(" ","").replace("\"","").rstrip().split("],[[")

    n = int(flds[0].replace("[[", ""))
    edges = [[int(col) for col in data.split(",")] for data in flds[1].replace("]]]", "").split("],[")]
    print("n = {0}".format(n))
    print("edges = {0}".format(edges))

    sl = Solution()
    time0 = time.time()

    result = sl.findSmallestSetOfVertices(n, edges)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
