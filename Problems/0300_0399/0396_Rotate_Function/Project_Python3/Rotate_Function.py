# coding: utf-8

import os
import sys
import time

class Solution:
#   def maxRotateFunction(self, A: List[int]) -> int:
    def maxRotateFunction(self, A):
        # 84ms
        total, res, lenA = 0, 0, len(A)
        for i in range(lenA):
            total += A[i]
            res += i * A[i]
        temp = res
        for i in range(lenA):
            if temp - total + A[i] * lenA > res:
                res = temp - total + A[i] * lenA
            temp = temp - total + A[i]*lenA
        return res

    def maxRotateFunction_work(self, A):
        # Time Limit Exceeded
        if A is None or len(A) <= 0:
            return 0
        lenA = len(A)
        res = [0]*lenA
        for i in range(lenA):
            for j in range(lenA):
                if i + j < lenA:
                    res[i] += (i + j)*A[j]
                else:
                    res[i] += (i + j - lenA)*A[j]
        return max(res)

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

    A = [int(n) for n in flds.split(",")]
    print("A = {0}".format(A))

    sl = Solution()

    time0 = time.time()

    result = sl.maxRotateFunction(A)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
