# coding: utf-8

import os
import sys
import time
import math
from functools import reduce

class Solution:
#   def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
    def prisonAfterNDays(self, cells: [int], N: int) -> [int]:
        # 32ms
        return reduce(lambda cells, j : [0] + [int(cells[i - 1] == cells[i + 1]) for i in range(1, 7)] + [0], [cells] + [0] * (N%14 and N%14 or 14))

    def prisonAfterNDays2(self, cells: [int], N: int) -> [int]:
        # 44ms
        seen = {str(cells): N}
        while N:
            seen.setdefault(str(cells), N)
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                N %= seen[str(cells)] - N
        return cells

    def prisonAfterNDays3(self, cells: [int], N: int) -> [int]:
        # Time Limit Exceeded.
        cellsLength = len(cells)
        for day in range(N):
            next = [0 for _ in range(cellsLength)]
            for i in range(1, cellsLength - 1):
                if cells[i - 1] == cells[i + 1]:
                    next[i] = 1
                else:
                    next[i] = 0
            cells = next
        return cells

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
    flds = temp.replace("\"","").replace(" ","").rstrip().split("],[")

    cells = [int(n) for n in flds[0].replace("[[", "").split(",")]
    N = int(flds[1].replace("]]", ""))
    print("cells = {0}, N = {1:d}".format(cells, N))

    sl = Solution()

    time0 = time.time()

    result = sl.prisonAfterNDays(cells, N)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
