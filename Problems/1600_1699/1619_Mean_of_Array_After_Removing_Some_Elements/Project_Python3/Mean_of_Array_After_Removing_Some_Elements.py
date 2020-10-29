# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def trimMean(self, arr: List[int]) -> float:
    def trimMean(self, arr):
        # 52ms
        n = len(arr)
        return sum(sorted(arr)[n // 20 : -n // 20]) / (n * 9 // 10)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    arr = [int(n) for n in flds.split(",")]
    print("arr = {0}".format(arr))

    sl = Solution()

    time0 = time.time()

    result = sl.trimMean(arr)

    time1 = time.time()

    print("result = {0:f}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
