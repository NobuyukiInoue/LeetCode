# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 464ms
        def valid(length):
            if not length: return True
            s = set([tuple(A[i : i + length]) for i in range(len(A) - length + 1)])
            return any(tuple(B[i : i + length]) in s for i in range(len(B) - length + 1))

        low, high = 0, min(len(A), len(B))
        while low < high:
            mid = (low + high) // 2 + 1
            if valid(mid):
                low = mid
            else:
                high = mid - 1
        return low

    def findLength2(self, A: List[int], B: List[int]) -> int:
        # 3744ms
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(row) for row in dp)

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
    B = [int(n) for n in flds[1].split(",")]
    print("A = {0}".format(A))
    print("B = {0}".format(B))

    sl = Solution()

    time0 = time.time()

    result = sl.findLength(A, B)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
