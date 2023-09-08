import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # 159ms - 173ms
        def helper(piles: List[int], dp: List[List[int]], suffixSum: List[int], i: int, M: int):
            if i == len(piles):
                return 0
            if i + 2 * M >= len(piles):
                return suffixSum[i]
            if dp[i][M] != 0:
                return dp[i][M]
            result = 0
            for x in range(1, 2 * M + 1):
                result = max(result, suffixSum[i] - helper(piles, dp, suffixSum, i + x, max(M, x)))
            dp[i][M] = result
            return result
        if not piles:
            return 0
        dp = [[0] * len(piles) for _ in range(len(piles))]
        suffixSum = [0] * len(piles)
        suffixSum[-1] = piles[-1]
        for i in range(len(piles) - 2, -1, -1):
            suffixSum[i] = piles[i] + suffixSum[i + 1]
        return helper(piles, dp, suffixSum, 0, 1)

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    piles = [int(n) for n in flds.split(",")]
    print("piles = {0}".format(piles))

    sl = Solution()

    time0 = time.time()

    result = sl.stoneGameII(piles)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
