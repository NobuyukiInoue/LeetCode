import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberOfPoints1(self, nums: List[List[int]]) -> int:
        # 73ms - 93ms
        lst = set()
        for start, end in nums:
            lst |= set(range(start, end + 1))
        return len(lst)

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # 92ms
        lst = set()
        for start, end in nums:
            for i in range(start, end + 1):
                lst.add(i)
        return len(lst)

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:2d}".format(grid[i][j]), end = "")
            else:
                print(",{0:2d}".format(grid[i][j]), end = "")
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    
    nums = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("nums", nums)

    sl = Solution()
    time0 = time.time()

    result = sl.numberOfPoints(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
