# coding: utf-8

import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 32ms
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(a) for a in zip(*mat[:: -1])]
        return False

    def findRotation11(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 40ms
        return len(set.intersection(*({k for k,x in enumerate((mat[i][j], mat[j][-i-1], mat[-i-1][-j-1], mat[-j-1][i])) if x==target[i][j]} for i in range(len(mat)) for j in range(len(mat))))) > 0

    def findRotation12(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 36ms
        return tuple(x for r in target for x in r) in zip(*([mat[i][j], mat[j][-i-1], mat[-i-1][-j-1], mat[-j-1][i]] for i in range(len(mat)) for j in range(len(mat))))

    def findRotation13(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 28ms
        return target in (mat, [*map(list, zip(*mat[::-1]))], [x[::-1] for x in mat][::-1], [*map(list, zip(*mat))][::-1])

    def findRotation14(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 32ms
        return target in (mat, (f := lambda M: [*map(list, zip(*M[::-1]))])(mat), f(f(mat)), f(f(f(mat))))

    def findRotation15(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 32ms
        return target in itertools.accumulate([mat] * 4, lambda m,_: [*map(list, zip(*m[::-1]))])

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
    flds = temp.replace(" ","").replace("\"","").replace("[[[","").replace("]]]","").rstrip().split("]],[[")

    mat = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
    target = [[int(col) for col in data.split(",")] for data in flds[1].split("],[")]
    printGrid("mat", mat)
    printGrid("target", mat)
  
    sl = Solution()
    time0 = time.time()

    result = sl.findRotation(mat, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
