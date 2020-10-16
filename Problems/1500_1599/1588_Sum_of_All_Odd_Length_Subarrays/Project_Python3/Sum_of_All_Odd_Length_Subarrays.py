# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    def sumOddLengthSubarrays(self, arr):
        # 32ms
        return sum(((i + 1)*(len(arr) - i) + 1)//2*num for i, num in enumerate(arr))

    def sumOddLengthSubarrays2(self, arr):
        # 60ms
        n = len(arr)
        res = 0
        for l in range(1, n + 1, 2):
            for i in range(n - l + 1):
                res += sum(arr[i:i + l])
        return res

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

    result = sl.sumOddLengthSubarrays(arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
