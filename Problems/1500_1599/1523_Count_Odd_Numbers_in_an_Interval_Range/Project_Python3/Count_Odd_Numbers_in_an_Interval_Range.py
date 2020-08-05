# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def countOdds(self, low: int, high: int) -> int:
    def countOdds(self, low, high):
        # 28ms
        return (high + 1) // 2 - low // 2

    def countOdds2(self, low, high):
        # 28ms
        if low % 2 == 0:
            s = low
        else:
            s = low - 1
        if high % 2 == 0:
            t = high
        else:
            t = high + 1
        return (t - s)//2

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    low, high = int(flds[0]), int(flds[1])
    print("low = {0:d}, high = {1:d}".format(low, high))

    sl = Solution()
    time0 = time.time()

    result = sl.countOdds(low, high)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
