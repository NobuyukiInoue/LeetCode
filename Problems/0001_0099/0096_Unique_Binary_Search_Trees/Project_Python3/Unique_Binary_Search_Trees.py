# coding: utf-8

import os
import sys
import time

class Solution:
#   def numTrees(self, n: int) -> int:
    def numTrees(self, n):
        # 32ms
        dp = [0]*(n + 5)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = 0
            for j in range(1, i + 1):
                dp[i] = dp[i] + dp[j - 1]*dp[i - j]
        return dp[n]

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
    n = int(temp.replace("[","").replace("]","").rstrip())
    print("num = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.numTrees(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
