# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#   def findCircleNum(self, M: List[List[int]]) -> int:
    def findCircleNum(self, M):
        # 176ms
        n = len(M)
        visited = set()
        ret = 0
        for i in range(n):
            if i not in visited:
                ret += 1
                q = [i]
                while q:
                    s = q.pop(0)
                    visited.add(s)
                    for j in range(n):
                        if M[s][j]==1 and j not in visited:
                            q.append(j)
                            visited.add(j)
        return ret


def printGrid(title, grid):
    if grid is None:
        print("{0} = []".format(title))
        return
    print("{0} = [".format(title))
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:d}".format(grid[i][j]), end = "")
            else:
                print(",{0:d}".format(grid[i][j]), end = "")
        print("]")
    print("]")

def printResult(title, result):
    print("{0} = [".format(title))
    for i in range(len(result)):
        print(result[i])
    print("]")

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    M = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("M", M)
  
    sl = Solution()
    time0 = time.time()

    result = sl.findCircleNum(M)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
