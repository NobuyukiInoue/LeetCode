# coding: utf-8

import math
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def largestSumOfAverages(self, A, K):
        # 156ms
        def rec(st, k):
            if (st, k) in cache:
                return cache[(st, k)]
            if k == 1:
                cache[(st, k)] = sum(A[st:])/(len(A)-st)
                return cache[(st, k)]
            total = 0
            res = -math.inf
            for i in range(st, len(A)-k+1):
                total += A[i]
                res = max(res, (total/(i-st+1)) + rec(i+1, k-1))
            cache[(st, k)] = res
            return cache[(st, k)]
        cache = {}
        return rec(0, K)

    def largestSumOfAverages2(self, A: List[int], K: int) -> float:
        # 232ms
        N = len(A)
        table = [[0]*K for _ in range(N)]
        minimum = min(A)
        summ = 0
        for i in range(N):
            summ += A[i]
            for j in range(K):
                if j == 0:
                    table[i][j] = summ/(i + 1)
                elif j >= i:
                    table[i][j] = summ
                else:
                    maximum = minimum
                    tmp = summ
                    for k in range(i):
                        tmp -= A[k]
                        res = table[k][j - 1] + tmp/(i - k)
                        if res > maximum:
                            maximum = res
                    table[i][j] = maximum
        return table[N - 1][K - 1]

    def largestSumOfAverages_bad(self, A: List[int], K: int) -> float:
        soretedA = sorted(A)
        leastA = soretedA[:len(soretedA) - K + 1]
        tops = soretedA[-(K - 1):]
        return sum(leastA)/len(leastA) + sum(tops)

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
    flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").rstrip().split("],[")
    A = [int(n) for n in flds[0].split(",")]
    K = int(flds[1])
    print("A = {0}, K = {1:d}".format(A, K))

    sl = Solution()

    time0 = time.time()

    result = sl.largestSumOfAverages(A, K)

    time1 = time.time()

    print("result = {0:f}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
