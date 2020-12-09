# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List,Dict,Tuple

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 56ms
        tripMap = collections.defaultdict(int)
        for row in trips:
            tripMap[row[1]] += row[0]
            tripMap[row[2]] -= row[0]
        tripList = sorted(tripMap.items(), key=lambda x:x[0])
        passengers = 0
        for data in tripList:
            passengers += data[1]
            if passengers > capacity:
                return False
        return True

    def carPooling2(self, trips: List[List[int]], capacity: int) -> bool:
        # 56ms
        for _, v in sorted(x for n, i, j in trips for x in [[i, n], [j, - n]]):
            capacity -= v
            if capacity < 0:
                return False
        return True

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
    flds = temp.replace("[[[","").replace("\"","").replace(" ","").rstrip().split("]],[")

    trips = [[int(n) for n in row.split(",")] for row in flds[0].split("],[")]
    capacity = int(flds[1].replace("]", ""))
    print("trips = {0}, capacity = {1:d}".format(trips, capacity))

    sl = Solution()

    time0 = time.time()

    result = sl.carPooling(trips, capacity)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
