# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def sumSubarrayMins(self, A: List[int]) -> int:
    def sumSubarrayMins(self, A: [int]) -> int:
        # 392ms
        MOD = 10**9 + 7
        lengthA = len(A)
        pre = [0]*lengthA
        helper = [0]*(lengthA + 1)
        for i, _ in enumerate(A):
            j = i - 1
            while j >= 0 and A[j] > A[i]:
                j = pre[j]
            pre[i] = j
            helper[i] = helper[j] + (i - j)*A[i]
        return sum(helper)%MOD

    def sumSubarrayMins2(self, A: [int]) -> int:
        # 552ms
        n, MOD = len(A), 10**9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])
        return sum(a * l * r for a, l, r in zip(A, left, right)) % MOD

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

    result = sl.sumSubarrayMins(A)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
