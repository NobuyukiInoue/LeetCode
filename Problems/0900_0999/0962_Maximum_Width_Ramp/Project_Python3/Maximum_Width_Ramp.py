# coding: utf-8

import bisect
import os
import sys
import time

class Solution:
#   def maxWidthRamp(self, A: List[int]) -> int:
    def maxWidthRamp(self, A):
        # 168ms
        stack = []
        res = 0
        for i in range(len(A))[::-1]:
            if not stack or A[i] > stack[-1][0]:
                stack.append([A[i], i])
            else:
                j = stack[bisect.bisect(stack, [A[i], i])][1]
                res = max(res, j - i)
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

    A = [int(n) for n in flds.split(",")]
    print("A = {0}".format(A))

    sl = Solution()
    time0 = time.time()
    result = sl.maxWidthRamp(A)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
