import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 212ms
        l1, l2 = len(word1), len(word2)
        if not word1 or not word1:
            return max(l1, l2)
        dp = [i for i in range(l2 + 1)]
        for i in range(l1):
            p = i + 1
            for j in range(l2):
                dp[j], p = p, dp[j] if word1[i] == word2[j] else min(p,dp[j + 1]) + 1
            dp[-1] = p
        return dp[-1]

    def minDistance2(self, word1: str, word2: str) -> int:
            # 300ms
            m, n = len(word1), len(word2)
            dp = [[0] * (n + 1) for i in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (word1[i] == word2[j]))
            return m + n - 2 * dp[m][n]

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
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    word1, word2 = flds[0], flds[1]
    print("word1 = {0}, word2 = {1}".format(word1, word2))

    sl = Solution()
    time0 = time.time()

    result = sl.minDistance(word1, word2)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
