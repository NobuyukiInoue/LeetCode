# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # 132ms - 198ms
        records = collections.defaultdict(int)
        for item in items1:
            records[item[0]] += item[1]
        for item in items2:
            records[item[0]] += item[1]
        ans = []
        for value in sorted(records.keys()):
            ans.append([value, records[value]])
        return ans

    def mergeSimilarItems_1liner(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # 164ms - 202ms
        return sorted((collections.Counter(dict(items1)) + collections.Counter(dict(items2))).items())

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

    items1 = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
    printGrid("items1", items1)
    items2 = [[int(col) for col in data.split(",")] for data in flds[1].split("],[")]
    printGrid("items2", items2)
  
    sl = Solution()
    time0 = time.time()

    result = sl.mergeSimilarItems(items1, items2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
