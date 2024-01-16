import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # 118ms - 138ms
        n = len(grid)
        cnts = [0 for _ in range(n*n + 1)]
        for row in grid:
            dic = collections.Counter(row)
            for key in dic:
                cnts[key] += dic[key]
        ans = [0, 0]
        for i in range(1, len(cnts)):
            if cnts[i] == 2:
                ans[0] = i
            elif cnts[i] == 0:
                ans[1] = i
        return ans

    def findMissingAndRepeatedValues2(self, grid: List[List[int]]) -> List[int]:
        # 136ms - 146ms
        n = len(grid)
        cnts = [0 for _ in range(n*n + 1)]
        for row in grid:
            for col in row:
                cnts[col] += 1
        ans = [0, 0]
        for i in range(1, len(cnts)):
            if cnts[i] == 2:
                ans[0] = i
            elif cnts[i] == 0:
                ans[1] = i
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
    print("grid = {0}".format(grid))

    sl = Solution()
    time0 = time.time()

    result = sl.findMissingAndRepeatedValues(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
