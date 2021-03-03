import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def longestPalindromeSubseq(self, s):
        # 516ms
        if s == s[::-1]:
            return len(s)
        n = len(s)
        dp = [0 for j in range(n)]
        dp[n - 1] = 1
        for i in range(n - 1, -1, -1):
            newdp = dp[:]
            newdp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j - 1]
                else:
                    newdp[j] = max(dp[j], newdp[j - 1])
            dp = newdp
        return dp[n - 1]

    def longestPalindromeSubseq2(self, s: str) -> int:
        # 3424ms
        n = len(s)
        DP = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[n - i] == s[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                else:
                    DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
        return DP[n][n]

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.longestPalindromeSubseq(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
