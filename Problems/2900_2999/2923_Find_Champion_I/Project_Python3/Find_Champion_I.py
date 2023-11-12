import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # 466ms - 484ms
        n = len(grid)
        for i in range(n):
            if sum(grid[i]) == n - 1:
                return i

    def findChampion2(self, grid: List[List[int]]) -> int:
        # 472ms - 487ms
        n = len(grid)
        for i, data in enumerate(grid):
            if sum(data) == n - 1:
                return i

    def findChampion3(self, grid: List[List[int]]) -> int:
        # 490ms
        ans, max_cnt = 0, 0
        for i, row in enumerate(grid):
            cnt = 0
            for _, col in enumerate(row):
                if col == 1:
                    cnt += 1
            if cnt > max_cnt:
                ans = i
                max_cnt = cnt
        return ans

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    
    grid = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print("grid = {0}\n".format(grid))

    sl = Solution()
    time0 = time.time()

    result = sl.findChampion(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
