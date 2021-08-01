# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # 176ms
        count_map = {}
        for row in wall:
            total = 0
            for i in range(len(row) - 1):
                total += row[i]
                count_map[total] = count_map.get(total, 0) + 1
        return len(wall) - (max(count_map.values()) if count_map.values() else 0)

    def leastBricks2(self, wall: List[List[int]]) -> int:
        # 172ms
        count_map = {}
        for row in wall:
            pos = 0
            for i in range(len(row) - 1):
                pos += row[i]
                if pos in count_map:
                    count_map[pos] += 1
                else:
                    count_map[pos] = 1
        max_pos = 0
        for _, v in count_map.items():
            max_pos = max(max_pos, v)
        return len(wall) - max_pos

    def leastBricks3(self, wall: List[List[int]]) -> int:
        # 184ms
        for row in wall:
            for i in range(1, len(row)):
                row[i] += row[i-1]
                
        count = collections.Counter(x for row in wall for x in row[:-1])
        return len(wall) - max(count.values()) if count else len(wall)

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    wall = [[int(n) for n in fld.split(",")] for fld in flds]
    print("wall = {0}".format(wall))

    sl = Solution()

    time0 = time.time()

    result = sl.leastBricks(wall)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
