# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # 60ms
        if K == 0 or N >= K + W - 1:
            return 1.0
        memo = [0] * (K + W - N) + [1] * (N - K + 1) + [(N - K + 1) / W]
        u, v = 1/W, 1 + 1/W
        for _ in range(K - 1):
            memo.append(v*memo[-1] - u*memo[~W])
        return memo[-1]

    def new21Game2(self, N: int, K: int, W: int) -> float:
        # 80ms
        if K == 0 or N >= K + W:
            return 1.0
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            if i < K:
                Wsum += dp[i]
            if i - W >= 0:
                Wsum -= dp[i - W]
        return sum(dp[K:])

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
    N, K, W = int(flds[0]), int(flds[1]), int(flds[2])
    print("N, K, W = {0:d}, {1:d}, {2:d}".format(N, K, W))

    sl = Solution()

    time0 = time.time()

    result = sl.new21Game(N, K, W)

    time1 = time.time()

    print("result = {0:f}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
