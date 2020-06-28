# coding: utf-8

import heapq
import os
import sys
import time

class Solution:
#    def distributeCandies(self, candies: List[int]) -> int:
    def distributeCandies(self, candies):
        return int(min(len(candies) / 2, len(set(candies))))

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
    flds = temp.replace("[","").replace("]","").rstrip()

    candies = [int(n) for n in flds.split(",")]
    print("candies = {0}".format(candies))

    sl = Solution()
    time0 = time.time()

    result = sl.distributeCandies(candies)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
