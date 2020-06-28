# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    def kWeakestRows(self, mat, k):
        # 108ms
        res = []
        for i in mat:
            res.append(sum(i))
        if len(res) == 0:
            return [0]
        ans = []
        for j in sorted(res):
            x = res.index(j)
            ans.append(x)
            res[x] = -1
        return ans[:k]

    def kWeakestRows2(self, mat, k):
        # 112ms
        return map(operator.itemgetter(1), sorted([(sum(x), i) for i, x in enumerate(mat)])[:k])

    def kWeakestRows3(self, mat, k):
        S = [[sum(g),i] for i,g in enumerate(mat)]
        R = sorted(S)
        return [r[1] for r in R[:k]]

def printGrid(title, grid):
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
    #    print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("[[[","").rstrip().split("]],[")

    mat = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
    k = int(flds[1].replace("]]", ""))
    printGrid("mat", mat)

    print("k = {0}".format(k))
  
    sl = Solution()
    time0 = time.time()
    result = sl.kWeakestRows(mat, k)

    time1 = time.time()

    if isinstance(result, map):
        print("result = {0}".format(list(result)))
    else:
        print("result = {0}".format(result))

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
