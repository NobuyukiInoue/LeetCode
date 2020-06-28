# coding: utf-8

import os
import sys
import time

class Solution:
#   def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
    def largestSumAfterKNegations(self, A, K):
        A.sort()
        for i in range(0, len(A)):
            if K == 0:
                return sum(A)
            if A[i] >= 0:
                break
            A[i] = -A[i]
            K -= 1
        A.sort()
        if K % 2 == 1:
            A[0] = -A[0]
        return sum(A)

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

    A = [int(n) for n in flds[0].split(",")]
    K = int(flds[1])
    print("A = {0}, K = {1:d}".format(A, K))

    sl = Solution()
    time0 = time.time()
    result = sl.largestSumAfterKNegations(A, K)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
