# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def getMaximumGenerated(self, n: int) -> int:
    def getMaximumGenerated(self, n: int) -> int:
        # 24ms
        arr, res = [], 0
        for i in range(n + 1):
            if i == 0: 
                arr.append(0)
                continue
            if i == 1: 
                arr.append(1)
                res = 1
            if 2 <= 2 * i <= n:
                arr.append(arr[i])
                res = max(res, arr[i])
            if 2 <= 2 * i + 1 <= n:
                val = arr[i] + arr[i + 1]
                arr.append(val)
                res = max(res, val)
        return res

    def getMaximumGenerated2(self, n: int) -> int:
        # 28ms
        if n < 2:
            return n
        A = [0, 1] + [0] * (n-1)
        for i in range(2, len(A)):
            if i & 1:
                A[i] = A[i//2] + A[i//2+1]
            else:
                A[i] = A[i//2]
        return max(A)

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
    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()

    time0 = time.time()

    result = sl.getMaximumGenerated(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
