# coding: utf-8

import json
import os
import sys
import time

class Solution:
#   def minSwap(self, A: List[int], B: List[int]) -> int:
    def minSwap(self, A: [int], B: [int]) -> int:
        # 84ms
        N = len(A)
        not_swap, swap = [N] * N, [N] * N
        not_swap[0], swap[0] = 0, 1
        for i in range(1, N):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap[i] = swap[i - 1] + 1
                not_swap[i] = not_swap[i - 1]
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                swap[i] = min(swap[i], not_swap[i - 1] + 1)
                not_swap[i] = min(not_swap[i], swap[i - 1])
        return min(swap[-1], not_swap[-1])

    def minSwap2(self, A: [int], B: [int]) -> int:
        # 128ms
        dp = [[-1 for j in range(2)] for i in range(len(A))]
        return self.helper(A, B, 0, dp, 0)

    def helper(self, A: [int], B: [int], index: int, dp: [[int]], state: int) -> int:
        if index == len(A):
            return 0
        if dp[index][state] != -1:
            return dp[index][state]
        min1, min2 = sys.maxsize, sys.maxsize
        if index == 0 or A[index - 1] < A[index] and B[index - 1] < B[index]:
            min1 = self.helper(A, B, index + 1, dp, 0)
        
        A[index], B[index] = B[index], A[index]

        if index == 0 or A[index - 1] < A[index] and B[index - 1] < B[index]:
            min2 = 1 + self.helper(A, B, index + 1, dp, 1)

        A[index], B[index] = B[index], A[index]

        dp[index][state] = min(min1, min2)
        return dp[index][state]

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
    A = [int(n) for n in flds[0].split(",")]
    B = [int(n) for n in flds[1].split(",")]
    print("A = {0}, B = {1}".format(A, B))

    sl = Solution()
    time0 = time.time()

    result = sl.minSwap(A, B)

    time1 = time.time()

    print("A = {0}, B = {1}".format(A, B))
    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
