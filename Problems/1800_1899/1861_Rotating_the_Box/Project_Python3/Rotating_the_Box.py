# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # 2385ms - 2433ms
        m, n = len(box), len(box[0])
        res = [["" for _ in range(m)] for _ in range(n)]
        for i in range(m):
            k = n - 1
            for j in range(n - 1, -1, -1):
                res[j][m - i - 1] = "."
                if box[i][j] != ".":
                    if box[i][j] == '*':
                        k = j
                    res[k][m - i - 1] = box[i][j]
                    k -= 1
        return res

def print_grid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0}".format(grid[i][j]), end = "")
            else:
                print(" {0}".format(grid[i][j]), end = "")
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    box = [[col for col in data.split(",")] for data in flds.split("],[")]
    print_grid("grid", box)
  
    sl = Solution()
    time0 = time.time()

    result = sl.rotateTheBox(box)

    time1 = time.time()

    print("result = {0}".format(result))
    print_grid("result", result)
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
