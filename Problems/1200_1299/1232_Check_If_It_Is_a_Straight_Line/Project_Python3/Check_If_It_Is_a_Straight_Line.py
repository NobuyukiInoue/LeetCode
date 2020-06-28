# coding: utf-8

import os
import sys
import time

import collections

class Solution:
#   def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    def checkStraightLine(self, coordinates):
        # 68ms
        dx = coordinates[1][0] - coordinates[0][0]
        if dx == 0:
            return False
        inclination = (coordinates[1][1] - coordinates[0][1]) / dx
        for i in range(1, len(coordinates) - 1):
            dx = coordinates[i+1][0] - coordinates[i][0]
            if dx == 0:
                return False
            if (coordinates[i+1][1] - coordinates[i][1]) / dx != inclination:
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    coordinates = [[int(col) for col in data.split(",")] for data in flds]
    print("coordinates = {0}".format(coordinates))

    sl = Solution()
    time0 = time.time()
    result = sl.checkStraightLine(coordinates)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
