# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    def findTheDistanceValue(self, arr1, arr2, d):
        # 116ms
        return sum(all(abs(a - b) > d for b in arr2) for a in arr1)

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

    arr1 = [int(col) for col in flds[0].split(",")]
    arr2 = [int(col) for col in flds[1].split(",")]
    d = int(flds[2])
    print("arr1 = {0}, arr2 = {1}, d = {2:d}".format(arr1, arr2, d))

    sl = Solution()
    time0 = time.time()
    result = sl.findTheDistanceValue(arr1, arr2, d)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
